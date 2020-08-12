import os
from os.path import isdir, join
from pathlib import Path
import librosa
import random
from fnmatch import fnmatch
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import keras
from keras import regularizers, callbacks
from keras.constraints import max_norm
from keras.models import Model, load_model
from keras.layers import Input, Lambda, Dense, Dropout, Activation
from keras.layers import Convolution2D, MaxPooling2D, LSTM, Conv2D
from keras.layers import BatchNormalization, TimeDistributed, Bidirectional
from keras.utils import np_utils

'''
# Record Audio
def recognizer():
	r = sr.Recognizer()
	with sr.Microphone() as source:
	    print("Say something!")
	    audio = r.listen(source)

	# Speech recognition using Google Speech Recognition
	try:
	    # for testing purposes, we're just using the default API key
	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	    # instead of `r.recognize_google(audio)`
	    value = r.recognize_google(audio)
	    print("You said: " + value)
	except sr.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
	    value = " "
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))
	    value = " "
	
	return value  
'''

# In[2]:
train_data_path = 'data/'


# In[3]:


def get_files(parent_path):
    files = os.listdir(parent_path)
    for i in files:
        if i ==".DS_Store":
            index1 = files.index(i)
            del files[index1]
        sub = ".wav"
        res = [j for j in files if sub in j]
        for k in res:
            index2 = files.index(k)
            del files[index2]
    files.sort()
    return files


# In[4]:


def one_hot(files):

    label_encoder = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(files)

    onehot_encoder = OneHotEncoder(categories='auto')
    onehot_encoder = onehot_encoder.fit_transform(integer_encoded.reshape(-1,1)).toarray()
    return onehot_encoder


# In[5]:


def read_audio(parent_path):
    wav_files = []
    directories = get_files(train_data_path)

    for audio_type_path in directories:
        for dirpath, dirname,files in os.walk(os.path.join(parent_path,audio_type_path)):
            for f in files:
                if fnmatch(f,"*wav"):
                    wav_files.append(os.path.join(dirpath,f))
    return wav_files


# In[7]:


def mfcc(wav_files,directories,label_onehot):
    X, sample_rate = librosa.load(wav_files)
    mfccs = librosa.feature.mfcc(X, sr = 16000, n_mfcc = 60)
    mfccs = np.mean(mfccs.T, axis = 0)
    mfccs = np.array(mfccs)
    return mfccs


# In[8]:


def label_class(wav_files,directories,label_onehot):
    for dire in directories:
        if dire in wav_files:
                index3 = directories.index(dire)
                label = label_onehot[index3]
                label = np.array(label)
    return label


# In[9]:


def keras_model(X_train,y_train,X_test,y_test,label_count):
    
    input_data = Input(name='the_input', shape=(None, X_train.shape[0]))

	conv_1d = Conv1D(filters, kernel_size, 
                     strides=conv_stride, 
                     padding=conv_border_mode,
                     activation=activation,
                     name='conv1d')(input_data)
    bn_cnn = BatchNormalization()(conv_1d)

	for i in range(conv_layers - 1):
        conv_1d = Conv1D(filters, kernel_size,
                         padding=conv_border_mode,
                         activation=activation,
                         dilation_rate=2**i,
                         name="conv_1d_"+str(i))(bn_cnn)
        bn_cnn = BatchNormalization()(conv_1d)
	
	brnn = Bidirectional(LSTM(units, activation=activation, 
        return_sequences=True, implementation=2, recurrent_dropout=0.02, name='brnn'))(bn_cnn)

	bn_rnn = BatchNormalization()(brnn)

	for i in range(recur_layers - 1):
        name = 'brnn_' + str(i + 1)
        brnn = Bidirectional(LSTM(units, activation=activation, 
        return_sequences=True, implementation=2, name=name))(bn_rnn)
        bn_rnn = BatchNormalization()(brnn)

	attentive = Attention()(bn_rnn)
	time_distributed_dense = TimeDistributed(Dense(1024))(attentive)
    time_dense = TimeDistributed(Dense(output_dim))(time_distributed_dense)

	softmax_layer = Activation('softmax', name='softmax')(time_dense)

	model = Model(inputs=input_data, outputs=softmax_layer)

	model.compile(loss='categorical_crossentropy', optimizer = 'adam' , metrics = ['accuracy'])

    model.fit(X_train, y_train, validation_data = (X_test, y_test), epochs= 500)

	train_loss, train_accuracy = model.evaluate(X_train,y_train)
    print("Train Accuracy = {}".format(train_accuracy))
    
    test_loss, test_accuracy = model.evaluate(X_test,y_test)
    print("Test Accuracy = {}".format(test_accuracy))
    
    return model	

# In[10]:


def main():
    
    data = []
    directories = get_files(train_data_path)
    label_count = int(len(directories))
    label_onehot = one_hot(directories)
    wav_files = read_audio(train_data_path)
    
    i = len(wav_files)
    j = 0
    k = 0
    
    for wav in wav_files:
        if j == 0:
            mfcc_data = [[mfcc(wav,directories,label_onehot)]]
            labels = [label_class(wav,directories,label_onehot)]
            data = mfcc_data
            label_classes = labels 
            j+=1
            continue
            
        mfcc_data= [[mfcc(wav,directories,label_onehot)]]
        labels = [label_class(wav,directories,label_onehot)]
        data = np.concatenate([data,mfcc_data], axis = 0)
        label_classes = np.concatenate([label_classes,labels], axis = 0)
        j+=1

    X_train, X_test, y_train, y_test = train_test_split(data, label_classes, test_size = 0.33)
    
    model = keras_model(X_train,y_train,X_test,y_test,label_count)

    model.save('ACVA_Model.h5')


# In[ ]:


if __name__ == "__main__":
    main() 


# In[12]:


model = keras.models.load_model('ACVA_Model.h5')


# In[21]:


model.summary()


# In[13]:


def mfcc_test(wav_files):
    X, sample_rate = librosa.load(wav_files)
    mfccs = librosa.feature.mfcc(X, sr = 16000,  n_mfcc = 60)
    mfccs = np.mean(mfccs.T, axis = 0)
    mfccs = np.array(mfccs)
    return mfccs


# In[19]:


def predict_model(model):
    
    test_file = 'test.wav'
    mfcc_wav_data = [[mfcc_test(test_file)]]

    predictions = model.predict([mfcc_wav_data])
    predictions = np.around(predictions)

    return predictions


# In[20]:


directories = get_files(train_data_path)
label_count = int(len(directories))
label_onehot = one_hot(directories)

prediction = predict_model(model)
print(prediction)
print('')

pred = "Word not found!"
for k in range(0,label_count):
    count = 0
    for i in range(0,label_count):
        if prediction.all() == label_onehot[k,i]:
            count+=1
            if count == label_count:
                pred = directories[k]
                break
            
print("The predicted word is: ",pred) 

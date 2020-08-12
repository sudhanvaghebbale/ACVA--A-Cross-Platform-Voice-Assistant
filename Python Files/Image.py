from PIL import Image, ImageDraw, ImageFont
from Windows_Exec import weather_information, rain_information, current_time


font_type = ImageFont.truetype("Fonts/Product Sans Regular.ttf",18)
font_type2 = ImageFont.truetype("Fonts/Product Sans Regular.ttf",22)
font_type1 = ImageFont.truetype("Fonts/Product Sans Regular.ttf",34)


def image1(data):
	image = Image.open("Images/label.png")
	draw = ImageDraw.Draw(image)
	if data == "Avengers":
		draw.text(xy=(100,30),text="Avengers Infinity War",fill=(0,0,0),font=font_type)
		draw.text(xy=(130,70),text="IMDb 8.5/10",fill=(0,0,0),font=font_type2)
		draw.text(xy=(80,100),text="Rotten Tomatoes 85%",fill=(0,0,0),font=font_type2)
		draw.text(xy=(60,130),text="Common Sense Media 5/5",fill=(0,0,0),font=font_type2)
		draw.text(xy=(110,160),text="Mediacritic 68%",fill=(0,0,0),font=font_type2)
		image.save("Label/Avengers/label.png")
	elif data == "Spanish":
		draw.text(xy=(120,30),text="In Spanish that is",fill=(0,0,0),font=font_type)
		draw.text(xy=(65,110),text="Hola, como estas",fill=(0,0,0),font=font_type1)
		image.save("Label/Spanish/label.png")
	elif data == "Spanish_Greet":
		draw.text(xy=(120,30),text="In Spanish that is",fill=(0,0,0),font=font_type)
		draw.text(xy=(60,110),text="Hola! Buenos Dias",fill=(0,0,0),font=font_type1)
		image.save("Label/Spanish_Greet/label.png")
	elif data == "Calculate":
		draw.text(xy=(150,30),text="Calculator",fill=(0,0,0),font=font_type)
		draw.text(xy=(100,110),text="9 * 2 + 3",fill=(0,0,0),font=font_type1)
		image.save("Label/Calculate/label.png")
	elif data == "Convert":
		draw.text(xy=(150,30),text="1 USD",fill=(0,0,0),font=font_type)
		draw.text(xy=(120,110),text="69.08 INR",fill=(0,0,0),font=font_type1)
		image.save("Label/Convert/label.png")
	elif data == "Bangalore":
		status,max,min,humid = weather_information()
		draw.text(xy=(100,30),text="Weather in Bangalore",fill=(0,0,0),font=font_type)
		draw.text(xy=(50,70),text="Status : %s" %(status),fill=(0,0,0),font=font_type2)
		draw.text(xy=(50,100),text="Maximum Temperature : %s" %(max),fill=(0,0,0),font=font_type2)
		draw.text(xy=(50,130),text="Minimum Temperature : %s" %(min),fill=(0,0,0),font=font_type2)
		draw.text(xy=(50,160),text="Humidity : %s" %(humid),fill=(0,0,0),font=font_type2)
		image.save("Label/Bangalore/label.png")
	elif data == "Rain":
		status,humid,clouds,text = rain_information()
		draw.text(xy=(100,30),text="Rain in Bangalore",fill=(0,0,0),font=font_type)
		draw.text(xy=(50,70),text="Will it Rain? : %s" %(text),fill=(0,0,0),font=font_type2)
		draw.text(xy=(50,100),text="Status : %s" %(status),fill=(0,0,0),font=font_type2)
		draw.text(xy=(50,130),text="Cloud Coverage: %s" %(clouds),fill=(0,0,0),font=font_type2)
		draw.text(xy=(50,160),text="Humidity : %s" %(humid),fill=(0,0,0),font=font_type2)
		image.save("Label/Rain/label.png")
	elif data == 'Umbrella':
		status,humid,clouds,text = rain_information()
		draw.text(xy=(100,30),text="Rain in Bangalore",fill=(0,0,0),font=font_type)
		draw.text(xy=(50,70),text="Umbrella : Better than getting wet later!",fill=(0,0,0),font=font_type1)
		draw.text(xy=(50,100),text="Status : %s" %(status),fill=(0,0,0),font=font_type2)
		draw.text(xy=(50,130),text="Cloud Coverage: %s" %(clouds),fill=(0,0,0),font=font_type2)
		draw.text(xy=(50,160),text="Humidity : %s" %(humid),fill=(0,0,0),font=font_type2)
		image.save("Label/Umbrella/label.png")
	elif data == 'Time':
		times = current_time()
		draw.text(xy=(100,30),text="Time in Bangalore",fill=(0,0,0),font=font_type)
		draw.text(xy=(120,110),text="%s" %(times),fill=(0,0,0),font=font_type1)
		image.save("Label/Time/label.png")
#image.save('Python.png')
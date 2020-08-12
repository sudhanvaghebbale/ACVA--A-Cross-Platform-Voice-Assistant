from selenium import webdriver


driver = webdriver.Chrome("C:/Users/Shwetha_Lokesh/Desktop/chromedriver.exe")
driver.get("https://www.google.com/search?q=play%20pacman")
class_play = driver.find_element_by_class_name('nvce1')
class_play.click()
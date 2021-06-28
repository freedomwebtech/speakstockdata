import requests
from bs4 import BeautifulSoup
import os
from gtts import gTTS




def speak(a):
    tts = gTTS(text=a, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")






name = input("search for companies:-")
url=requests.get('https://www.google.com/search?q='+str(name)+'+share+price')
soup = BeautifulSoup(url.text,'lxml')
a=soup.select('div',class_=" IsqQVc NprOob XcVN5d wT3VGc")[104].getText()
h=(a).replace("Disclaimer","").replace("Stock Price","stock price is  ").replace("/","")
print(h)
speak(h)




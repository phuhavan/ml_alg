from gtts import gTTS
import os

# Simple sentence
textContent = 'Hello, I am alias of Phu, who is currently PhD student at INRIA'

# Complex one, a paragraph of an article
with open('article.txt', 'r') as myFile:
    data=myFile.read()

# Complex Vietnamese text
with open('vietnamese.txt', 'rb') as myVietnameseText:
    vietnamese=myVietnameseText.read().decode('utf8', 'ignore')

tts = gTTS(text=vietnamese,lang='vi')
tts.save("sample.mp3")
os.system("mpg123 sample.mp3")
os.system("rm sample.mp3")


import Image
from pytesseract import image_to_string
from gtts import gTTS 
import os 

print image_to_string(Image.open('im.jpg'), lang='eng')

mytext = image_to_string(Image.open('im.jpg'), lang='eng')
language = 'en' 
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("welcome.mp3") 
os.system("mpg321 welcome.mp3") 

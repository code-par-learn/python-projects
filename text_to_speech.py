
from pickle import TRUE
from gtts import gTTS
from playsound import playsound

testread=open("Output1.txt")    
lang_en="en"
call=gTTS(text=testread.read(),lang=lang_en,slow=TRUE)
call.save("welcome2.mp3")
playsound("welcome2.mp3")
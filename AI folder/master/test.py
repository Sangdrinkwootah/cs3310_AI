import speech_recognition as sr
import wikipedia
wikipedia.set_lang('vi')
language = 'vi'
recognizer = sr.Recognizer()
from gtts import gTTS
import os

''' recording the sound '''
from gtts import gTTS
import os
mytext = "ĐM THẰNG 34!"
audio = gTTS(text=mytext, lang="vi", slow=False)
audio.save("example.mp3")
os.system("start example.mp3")

with sr.Microphone() as source:
    print("Adjusting noise ")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Recording for 10 seconds")
    recorded_audio = recognizer.listen(source, timeout=10)
    print("Done recording")

''' Recorgnizing the Audio '''
try:
    print("Recognizing the text")
    text = recognizer.recognize_google(
            recorded_audio, 
            language="vi"
        )
    print("Decoded Text : {}".format(text))

except Exception as ex:
    print(ex)
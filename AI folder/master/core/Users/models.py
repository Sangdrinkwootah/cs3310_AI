import speech_recognition as sr
import wikipedia
wikipedia.set_lang('vi')
language = 'vi'
recognizer = sr.Recognizer()
from gtts import gTTS
import os

# ''' recording the sound '''
# from gtts import gTTS
# import os
# mytext = "ultr"
# audio = gTTS(text=mytext, lang="vi", slow=False)
# audio.save("example.mp3")
# os.system("start example.mp3")

class Users:
    def setName(self, name):
        # Voice recognition user's name
        with sr.Microphone() as source:
            print("Adjusting noise ")
            recognizer.adjust_for_ambient_noise(source, duration = 1)
            print("What is your name?")
            recorded_audio = recognizer.listen(source, timeout = 5)
            print("Done recording")

        ''' Recognizing the Audio '''
        try:
            # print("Recognizing the text")
            name = recognizer.recognize_google(
                    recorded_audio, 
                    language="vi"
                )
            print("Your name is {}".format(name))
            f = open("User Info\\name.txt", "a")
            f.write(name)
            f.close()

        except Exception as ex:
            print(ex)
        return 

    # Voice recognition user's age 
    with sr.Microphone() as source:
        print("Adjusting noise ")
        recognizer.adjust_for_ambient_noise(source, duration = 1)
        print("How old are you?")
        recorded_audio = recognizer.listen(source, timeout = 10)
        print("Done recording")

    ''' Recognizing the Audio '''
    try:
        # print("Recognizing the text")
        age = recognizer.recognize_google(
                recorded_audio, 
                language="vi"
            )
        print("You are {} year(s) old".format(age))
        f = open("User Info\\age.txt", "a")
        f.write(age)
        f.close()

    except Exception as ex:
        print(ex)

    # Voice recognition user's weight    
    with sr.Microphone() as source:
        print("Adjusting noise ")
        recognizer.adjust_for_ambient_noise(source, duration = 1)
        print("What is your weight? (in kilograms)")
        recorded_audio = recognizer.listen(source, timeout = 10)
        print("Done recording")

    ''' Recognizing the Audio '''
    try:
        # print("Recognizing the text")
        weight = recognizer.recognize_google(
                recorded_audio, 
                language="vi"
            )
        print("You are {} kg(s)".format(weight))
        f = open("User Info\\weight.txt", "a")
        f.write(weight)
        f.close()

    except Exception as ex:
        print(ex)

    # Voice recognition user's height    
    with sr.Microphone() as source:
        print("Adjusting noise ")
        recognizer.adjust_for_ambient_noise(source, duration = 1)
        print("What is your height? (in centimeters)")
        recorded_audio = recognizer.listen(source, timeout = 10)
        print("Done recording")

    ''' Recognizing the Audio '''
    try:
        # print("Recognizing the text")
        height = recognizer.recognize_google(
                recorded_audio, 
                language="vi"
            )
        print("You are {} cm(s)".format(height))
        f = open("User Info\\height.txt", "a")
        f.write(height)
        f.close()

    except Exception as ex:
        print(ex)

    # Voice recognition user's gender   
    with sr.Microphone() as source:
        print("Adjusting noise ")
        recognizer.adjust_for_ambient_noise(source, duration = 1)
        print("What is your gender?")
        recorded_audio = recognizer.listen(source, timeout = 10)
        print("Done recording")

    ''' Recognizing the Audio '''
    try:
        # print("Recognizing the text")
        gender = recognizer.recognize_google(
                recorded_audio, 
                language="vi"
            )
        print("You are {}".format(name))
        f = open("User Info\\gender.txt", "a")
        f.write(gender)
        f.close()

    except Exception as ex:
        print(ex)

    # Voice recognition user's hobby    
    with sr.Microphone() as source:
        print("Adjusting noise ")
        recognizer.adjust_for_ambient_noise(source, duration = 1)
        print("What food do you like?\n(Eg:I like meat, I like beef,..)")
        recorded_audio = recognizer.listen(source, timeout = 10)
        print("Done recording")

    ''' Recognizing the Audio '''
    try:
        # print("Recognizing the text")
        hobby = recognizer.recognize_google(
                recorded_audio, 
                language="vi"
            )
        print("You likes {}".format(hobby))
        f = open("User Info\\hobby.txt", "a")
        f.write(hobby)
        f.close()

    except Exception as ex:
        print(ex)


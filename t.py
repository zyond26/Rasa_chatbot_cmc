import requests
import speech_recognition as sr
import pyttsx3
from gtts import gTTS
from translate import Translator

converter = pyttsx3.init()
converter.setProperty('rate', 150)
converter.setProperty('volume', 0.7)
voices = converter.getProperty('voices')
converter.setProperty('voice', voices[1].id)

rec = sr.Recognizer()

bot_message = ""

while (True):
    with sr.Microphone(device_index=0) as source:
        print("Đại học Khoa học Huế đang nghe...")
        message = rec.listen(source)

    try:
        query = rec.recognize_google(message, language="vi")
        print("Bạn nói : {}".format(query))
        r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": query})

        for i in r.json():
            print("Bot nói  : {}".format(i['text']))
            bot_message = i['text']
          #  bot_message = gTTS(bot_message,lang='vi',slow=False)
            converter.say(bot_message)
            converter.runAndWait()

    except Exception as e:
        converter.say(e)
        converter.runAndWait()
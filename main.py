import pyttsx3
import requests

# _______________________________VARIABLES_AND_CONSTANTS__________________________
INTRO = "Hey There Today's News is brought to you by Prathamesh who is famous hacker. " \
        "Stop Laughing and start Listening the news. And dont forget to say thankyou"
ENDPOINT = "http://newsapi.org/v2/everything"
API_KEY = "753b000d70cf464f80645f6737803ddf"
language = "en"
title_speak = ""
description_speak = ""


# ______________________________________FROM_PYTTSX_3_MODULE____________________________________
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


rate = engine.getProperty('rate')
engine.setProperty('rate', 165)
# ______________________________________GET_THE_NEWS__________________________________________
parameters = {
    "qInTitle": "python OR cplusplus OR coding OR development OR development hacks",
    "apiKey": API_KEY
}
response = requests.get(url=ENDPOINT, params=parameters)
articles = response.json()["articles"]

engine.say(INTRO)
for article in articles:
    title_speak = article["title"]
    description_speak = article["description"]
    news = f"{title_speak} now In Brief {description_speak}"
    engine.say(news)
    engine.say("Now Headover to the next news!")
    engine.runAndWait()
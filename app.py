# this is about creating a dictionary in python using the given data.

import json
from difflib import get_close_matches
import speech_recognition as sr

data = json.load(open("data.json"))

# take word as voice input from user.
def word_voice_find():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        word = r.recognize_google(audio)
        word = word.lower()
        uword = word.title()
        if word in data:
            for i in data[word]:
                print(word+" means "+i)
        elif uword in data:
            for i in data[uword]:
                print(uword+" means "+i)
        else:
            poss = get_close_matches(word,data.keys(),1,0.8)
            if len(poss) == 0:
                print("Well is that even a word!")
            else:
                for i in data[poss[0]]:
                    print(poss[0]+" means "+i)
    except sr.UnknownValueError:
        print("We couldn't get what you are trying to say!")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
# take word as input from user
def word_keyboard_find():
    print("\n")
    word = input("Enter a word: ")
    word = word.lower()
    uword = word.title()
    if word in data:
        for i in data[word]:
            print(i)
    elif uword in data:
        for i in data[uword]:
            print(i)
    else:
        poss = get_close_matches(word,data.keys())
        if len(poss) > 0:
            print("It seems you have misspelled")
            for i in poss:
                print(i)
            ch = input("Enter Y/N: ")
            if ch == 'y':
                word_find()
        else:
                print("Well is "+word+" even a word?")

# take user's choice either voice or traditional input.

choice = input("Great! So how are you planning to use this app?"+
"\n press 1 for keyboard input"+
"\n press 2 for voice input")

if choice == '1':
    word_keyboard_find()
elif choice == '2':
    word_voice_find()
else:
    print("I guess you have made a wrong choice! You need to start over again")

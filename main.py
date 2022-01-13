from translate import Translator
from gtts import gTTS
import gtts
from playsound import playsound
import os
import json

with open('./resources/languages.json', 'r+') as langfile:
    langs = json.loads(langfile.read())

temp = './resources/temp.mp3'
print('Please enter your language (2-letter ISO)')
gTTS('Please enter your language in 2 letter I S O format').save('./resources/temp.mp3')
playsound('./resources/temp.mp3')
os.remove(temp)
while True:
    from_lang = input()
    if from_lang in langs.values():
        break
    else:
        print('Invalid Language. Please Try Again')
        gTTS('Invalid Language. Please Try Again').save('./resources/temp.mp3')
        playsound('./resources/temp.mp3')
        os.remove(temp)

print('Please enter the language to translate to (2-letter ISO)')
gTTS('Please enter the target language in 2 letter I S O format').save(temp)
playsound(temp)
os.remove(temp)
while True:
    to_lang = input()
    if to_lang in langs.values():
        break
    else:
        print('Invalid Language. Please Try Again')
        gTTS('Invalid Language. Please Try Again').save('./resources/temp.mp3')
        playsound('./resources/temp.mp3')
        os.remove(temp)
print('Please enter the sentence to translate')
gTTS('Please enter the sentence you want to translate').save(temp)
playsound(temp)
os.remove(temp)
sentence = input()
print(Translator(from_lang=from_lang, to_lang=to_lang).translate(sentence))
if to_lang in gtts.lang.tts_langs().keys():
    gTTS(Translator(from_lang=from_lang, to_lang=to_lang).translate(sentence), lang=to_lang).save(temp)
    playsound(temp)
    os.remove(temp)
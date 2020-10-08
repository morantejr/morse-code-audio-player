#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 20:41:36 2020

@author: josephmorante
"""
#Translate word into morse code
#Dictionary holds the key  
from playsound import playsound
import time


langs = "en"


cipher = {'A':'.-','B':'-...','C':'-.-.',
          'D':'-..','E':'.','F':'..-.',
          'G':'--.','H':'....','I':'..',
          'J':'.---','K':'-.-','L':'.-..',
          'M':'--','N':'-.','O':'---',
          'P':'.--.','Q':'--.-','R':'.-.',
          'S':'...','T':'-','U':'..-',
          'V':'...-','W':'.--','X':'-..-',
          'Y':'-.--','Z':'--..','0':'-----',
          '1':'.----','2':'..---','3':'...--',
          '4':'...-','5':'.....','6':'-....',
          '7':'--...', '8':'---..','9':'----.', 
          ' ': '/', '?':'..--..','.':'.-.-.-',
          ',':'--..--', '!':'-.-.--'}

#Takes in user's message
message = list(input('Please put in a sentence: '))

#loops through message to make them upper(1/20/20 replaced for loop with list comprehension)
#Makes it possible to translate


#holder for morse code message
#code = ''
code = [cipher[i.upper()] + ' ' for i in message]

#Joins the message and does not appear as an array anymore
morse = ''.join(code)

for m in morse:
    if m == '.':
        playsound('/Users/josephmorante/Downloads/Work/Program_Projects/python_scripts/dit.wav')
    elif m == '-':
        playsound('/Users/josephmorante/Downloads/Work/Program_Projects/python_scripts/dah.wav')
 ##b      time.sleep(0.5)
#sucmorse_speech = gTTS(text=code, lang = langs, slow=False)



#Try & Exception to state issue
try:
    print(f'{morse}')

except KeyError as ke: 
    print(f'{ke}')


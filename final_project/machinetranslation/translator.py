'''This module contains two function to translate from en to fr and from fr to en'''
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    '''Translate from en to fr'''
    #write the code here
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text

def french_to_english(french_text):
    '''Translate from fr to en'''
    #write the code here
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text

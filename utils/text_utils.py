# utils/text_utils.py
import re
import string

class TextCleaner:
    @staticmethod
    def remove_punctuation(text):
        return text.translate(str.maketrans('', '', string.punctuation))
    
    @staticmethod
    def to_lower(text):
        return text.lower()
    
    @staticmethod
    def split_sentences(text):
        return re.split(r'[。！？.!?]', text)
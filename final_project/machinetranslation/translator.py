"""convert english and french texts"""
from deep_translator import MyMemoryTranslator

def englishToFrench(english_text):
    """Convert english text to french"""
    french_text = MyMemoryTranslator(source="en-GB", target="fr-FR").translate(english_text)
    return french_text

def frenchToEnglish(french_text):
    """ Convert french text to english """
    english_text = MyMemoryTranslator(source="fr-FR", target="en-GB").translate(french_text)
    return english_text



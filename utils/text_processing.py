from transformers import pipeline
from langdetect import detect
import re

# Initialize pipelines globally within the module
translator_ml_en = pipeline("translation", model="Helsinki-NLP/opus-mt-ml-en")
translator_en_ml = pipeline("translation", model="Helsinki-NLP/opus-mt-en-ml")
text_generator = pipeline("text-generation", model="alpindale/gemma-2b-it")

def translate_ml_to_en(text):
    """Translates Malayalam text to English."""
    sentences = re.split(r'(?<=[\.\?\!])\s+', text)
    translated_sentences = [translator_ml_en(sentence)[0]['translation_text'] for sentence in sentences]
    return ' '.join(translated_sentences)

def translate_en_to_ml(text):
    """Translates English text to Malayalam."""
    sentences = re.split(r'(?<=[\.\?\!])\s+', text)
    translated_sentences = [translator_en_ml(sentence)[0]['translation_text'] for sentence in sentences]
    return ' '.join(translated_sentences)

def generate_text(text):
    """Generates text based on the input."""
    return text_generator(text, max_length=50)[0]['generated_text']

def process_text(original_text):
    """Processes the text based on language and generates responses."""
    detected_language = detect(original_text)

    if detected_language == 'ml':
        english_text = translate_ml_to_en(original_text)
    else:
        english_text = original_text

    generated_text = generate_text(english_text)
    malayalam_response = translate_en_to_ml(generated_text)

    return english_text, generated_text, malayalam_response
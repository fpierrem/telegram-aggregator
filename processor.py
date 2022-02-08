from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import re

translation_tokenizer = AutoTokenizer.from_pretrained("translation_model_saved")
translation_model = AutoModelForSeq2SeqLM.from_pretrained("translation_model_saved")

summarizer_tokenizer = AutoTokenizer.from_pretrained("google-pegasus-xsum")
summarizer_model = AutoModelForSeq2SeqLM.from_pretrained("google-pegasus-xsum")

def summarize(message):
    inputs = summarizer_tokenizer(message,return_tensors="pt")
    outputs = summarizer_model.generate(inputs["input_ids"])
    processed_text = summarizer_tokenizer.decode(outputs[0])
    summary = re.sub('</s>','',processed_text)
    return summary

def translate(message):
    inputs = translation_tokenizer(message,return_tensors="pt")
    outputs = translation_model.generate(inputs["input_ids"])
    processed_text = translation_tokenizer.decode(outputs[0])
    translation = re.sub('</s>','',processed_text)
    return translation

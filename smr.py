from bs4 import BeautifulSoup
import requests
import re
import streamlit as st
import csv
import pandas as pd
from transformers import PegasusTokenizer, PegasusForConditionalGeneration
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline


@st.cache_resource
def model_init():
    model_name = "human-centered-summarization/financial-summarization-pegasus"
    tokenizer = PegasusTokenizer.from_pretrained(model_name)
    model = PegasusForConditionalGeneration.from_pretrained(model_name)

    return tokenizer, model


def semmer():
    with open("transcript3.txt", "r") as file:
        transcrpt = file.read()
    sum = []
    ARTICLE = transcrpt
    max_chunk = 450
    ARTICLE = ARTICLE.replace('.', '.<eos>')
    ARTICLE = ARTICLE.replace('?', '?<eos>')
    ARTICLE = ARTICLE.replace('!', '!<eos>')
    sentences = ARTICLE.split('<eos>')
    current_chunk = 0
    chunks = []
    for sentence in sentences:
        if len(chunks) == current_chunk + 1:
            if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:
                chunks[current_chunk].extend(sentence.split(' '))
            else:
                current_chunk += 1
                chunks.append(sentence.split(' '))
        else:
            print(current_chunk)
            chunks.append(sentence.split(' '))

    for chunk_id in range(len(chunks)):
        chunks[chunk_id] = ' '.join(chunks[chunk_id])

    summaries = []
    tokenizer, model = model_init()
    for text in chunks:
        input_ids = tokenizer.encode(
            text, return_tensors='pt', max_length=512, truncation=True)
        output = model.generate(
            input_ids, max_length=55, num_beams=3, early_stopping=True)
        summary = tokenizer.decode(output[0], skip_special_tokens=True)
        summaries.append(summary)

        a = ' '.join([summ for summ in summaries])
        sum.append(a)

    return sum

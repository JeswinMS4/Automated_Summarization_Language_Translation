import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
from googletrans import Translator
from smr import semmer
import requests
import time


translater = Translator()


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_url_icon = "https://lottie.host/dd4520d5-1c79-4b42-976c-39712218dfed/tILq1mCuAh.json"
lottie_icon = load_lottieurl(lottie_url_icon)
st_lottie(lottie_icon, key='Hey')

st.title("Knowledge Based model on Text Summarization and Translation: ")

audio_file = open('final.mp3', 'rb')
audio_bytes = audio_file.read()
st.header('Summarization ')
textorig = st.text_area('Enter the text here:📝', height=200)
with open("transcript3.txt", "w") as file:
    file.write(textorig)

st.audio(audio_bytes, format='audio/mp3')
sumerise = st.button("Summarise")
if (sumerise):
    summary = semmer()
    st.markdown(summary)
    st.snow()
st.header('Translator 😄')
colsa, colsb = st.columns([1, 2])
with colsa:
    lottie_url_icon = "https://lottie.host/e5204481-ff48-4af5-b835-a4fee0832bfa/uUm4hC3kmM.json"
    lottie_icon = load_lottieurl(lottie_url_icon)

    st_lottie(lottie_icon, key='Translate')
with colsb:
    enterorg = st.text_area("Enter the text to be translated:💥")
    option = st.selectbox(
        'Which language do you want to translate it to?',
        ('', 'Hindi', 'Kannada', 'English', 'Telugu', 'Malayalam', 'Tamil', 'French', 'Japanese'))
    trns = st.button('Translate')
    if (trns):
        if (option == 'Hindi'):
            out = translater.translate(enterorg, dest="hi")
            st.write(out.text)
        elif (option == 'Kannada'):
            out = translater.translate(enterorg, dest="kn")
            st.write(out.text)
        elif (option == 'English'):
            out = translater.translate(enterorg, dest="en")
            st.write(out.text)
        elif (option == 'Telugu'):
            out = translater.translate(enterorg, dest="te")
            st.write(out.text)
        elif (option == 'Malayalam'):
            out = translater.translate(enterorg, dest="ml")
            st.write(out.text)
        elif (option == 'Tamil'):
            out = translater.translate(enterorg, dest="ta")
            st.write(out.text)
        elif (option == 'French'):
            out = translater.translate(enterorg, dest="fr")
            st.write(out.text)
        elif (option == 'Japanese'):
            out = translater.translate(enterorg, dest="ja")
            st.write(out.text)

lottie_url_icon = "https://lottie.host/311a5565-842f-4f6a-8ac7-fdc069377b90/CfnFiB9Uwy.json"
lottie_icon = load_lottieurl(lottie_url_icon)
st_lottie(lottie_icon, key='End')

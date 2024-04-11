import streamlit as st
from googletrans import Translator

st.header('Machine Translation Demo')
input = st.text_area("Please enter the text", value="") #text box single line, #text area multiple line
option = st.selectbox(
    'Tp which language you wish to translate this to?',
    ('Malayalam','Hindi','Tamil','Bengali'))
if st.button("Translate"):
    translator = Translator()
    translation = translator.translate(input, dest=option) #dest will see in which language is needs to be translated that user have chosen
    st.write(translation.text)
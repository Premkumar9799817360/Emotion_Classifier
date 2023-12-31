# Core Pkgs
import streamlit as st 
import pickle
import pandas as pd 
import numpy as np 
import base64
# import joblib 
# pipe_lr = joblib.load(open("emotion_classifier.pkl","rb"))

pipe_lr = pickle.load(open('emojy_model.pkl','rb'))
st.title("Emojy Prediction System")
input_sms = st.text_area("Enter the message")
emotions_emoji_dict = {"anger":"😠","disgust":"🤮", "fear":"😨😱", "happy":"🤗", "joy":"😂", "neutral":"😐", "sad":"😔", "sadness":"😔", "shame":"😳", "surprise":"😮"}
if st.button('Predict'):
   
    result = pipe_lr.predict([input_sms])[0]
    # print(result)
    # Display
    if result =='joy':
        st.title("😂")
        st.header("Joy")
    elif result == 'anger':
        st.title("😠")
        st.header("Anger")
    elif result == 'fear':
      st.title("😨😱")
      st.header("Fear")
    elif result == 'neutral':
      st.title("😐")
      st.header("Neutral")
    elif result == 'sadness':
      st.title("😔")
      st.header("Sadness")
    elif result == 'shame':
       st.title("😳")
       st.header("Shame")
    elif result == 'disgust':
       st.title("🤮")
       st.header("Disgust")
    elif result == 'surprise':
       st.title("😮")
       st.header("Surprise")
    else:
       st.title("🤗")
st.header("Created By Prem Kumar")
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('image.jpg')

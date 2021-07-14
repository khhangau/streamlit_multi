import streamlit as st
from multiapp import MultiApp
import pandas as pd
import base64
from PIL import Image

def app():
    st.header('Mitchelton AL Recorded H versus Modelled Q')
    st.image(Image.open("2015_CTC.png"))

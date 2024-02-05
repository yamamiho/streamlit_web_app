import streamlit as st
from PIL import Image

#image
st.subheader("画像")
img = Image.open("/home/yamamotomiho/program/python/homepage/aikon.jpg")
st.image(img,width=200)

"""
@author: idoia lerchundi
"""
import streamlit as st
from PIL import Image,ImageFile
import numpy as np
import requests
from io import BytesIO
from streamlit_component_fill_square_cropper101 import fill_square_cropper #using local
#import streamlit_component_fill_square_cropper101 as stcropper

#streamlit_component_fill_square_cropper101._DEBUG = True

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        

st.set_page_config(
   page_title="Streamlit iCodeIdoia",
   page_icon="images/ilpicon1.png",layout="wide",initial_sidebar_state="expanded"
)
st.image("images/banner.jpg")

# ---- LOAD
local_css("styles/style.css")

def main() -> None:

 with st.sidebar:
        st.image("images/modern.png")
        st.markdown("---")
        st.markdown(
            'Created by <a href="https://webdevserv.github.io/html_bites/dev/webdev.html" target="_blank">webdevserv</a>',
            unsafe_allow_html=True,
        )
        st.markdown(
            'Github: <a href="https://github.com/webdevserv/streamlit_component_fill_square_cropper101/blob/main/README.md" target="_blank">README.md</a>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div style="margin: 0.75em 0;"><a href="https://www.buymeacoffee.com/Artgen" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a></div>',
            unsafe_allow_html=True,
        )
 # ---- TABS
 tab1, tab2 = st.tabs(["Demo","Application"])

 with tab1:   
   # Handle first image
   url = "https://raw.githubusercontent.com/webdevserv/images_video/main/cowportrait.jpg" 
   # Handle second image
   url2 = "https://raw.githubusercontent.com/webdevserv/images_video/main/cowlandscape.jpg"

   st.subheader("Fill, square an image demo")
   img_description = st.text('Image will be squared with color filler where applicable.')

   if st.button('Square and Fill Demo'):  
     response = requests.get(url)
     img = Image.open(BytesIO(response.content))
     img.load()

     generated_img = fill_square_cropper(img)
     st.image(generated_img)

     response = requests.get(url2)
     img = Image.open(BytesIO(response.content))
     img.load()

     generated_img = fill_square_cropper(img)
     st.image(generated_img)
   
 with tab2:
   st.subheader("Square an image app")
   img_description = st.text('Image will be squared with color filler where applicable.')
   uploaded_file = st.file_uploader("Upload a JPG image to square and fill with color.", type=['jpg'])

   if uploaded_file is not None: 
     img = Image.open(uploaded_file)
     img.load()
     generated_img = fill_square_cropper(img)
     st.image(generated_img)


if __name__ == "__main__":
  main()

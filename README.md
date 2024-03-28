# streamlit_component_fill_square_cropper - Demo

streamlit_component_fill_square_cropper demo on Streamlit Sharing

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://webdevserv-portfolio-idoia-icodeidoia-portfolio-9kblei.streamlit.app/LIVE_Square_Filler_app)

# streamlit_component_fill_square_cropper - Example app.py

   # Handle first image
   url = "https://.../cowportrait.jpg" 
   # Handle second image
   url2 = "https://.../cowlandscape.jpg"
   
   st.subheader("Fill square an image demo")
   img_description = st.text('Image will be squared with color filler where applicable.')

   if st.button('Square and Fill Demo'):  
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.load()

    generated_img = imported_fill_square_cropper(img)
    st.image(generated_img)

    response = requests.get(url2)
    img = Image.open(BytesIO(response.content))
    img.load()

    generated_img = imported_fill_square_cropper(img)
    st.image(generated_img)

import streamlit as st

st.write("Displaying an local Images")

# Displaying Image by specifying path
st.image("files/animal7.jpg")

# Image Courtesy by unplash
st.write("Image Courtesy: unplash.com")

###################################################

st.write("Displaying an URL Images")

# Displaying Image by specifying path
st.image("https://tinyurl.com/322vu3ab")

# Image Courtesy
st.write("Courtesy: unplash.com")

#####################################################

# Image Courtesy
st.write("Siplaying Multiple Images")

# Listing out animal images
animal_images = [
    'files/animal1.jpg',
    'files/animal2.jpg',
    'files/animal3.jpg',
    'files/animal4.jpg',
    'files/animal5.jpg',
    'files/animal6.jpg',
    'files/animal7.jpg',
    'files/animal8.jpg',
    'files/animal9.jpg',
    'files/animal10.jpg'
   
]

# Displaying Multiple images with width 150
st.image(animal_images, width=150)

# Image Courtesy
st.write("Image Courtesy: Unplash")
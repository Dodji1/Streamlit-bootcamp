import streamlit as st

# Open Audio using filepath with filename 
sample_audio = open("files/audio.wav", "rb")

#Reading Audio File
audio_bytes = sample_audio.read()

# Display Audio using st.audio() function with start time set to 20
st.audio(sample_audio, start_time = 20)

# Printing Audio Courtesy
st.write("Audio Courtesy: https://file-examples.com/index.php/sample-audio-files/sample-wav-download/")

########################################################

# Open Audio using filepath with filename and read the audio file
sample_url = st.audio("https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba.mp3")

st.write("Audio Courtesy: https://www.learningcontainer.com/sample-audio-file/")

######################################################

# Displaying Video using youtube URL
st.video("https://www.youtube.com/watch?v=OMkEVX23BdM")

# Courtesy by youtube channel
st.write("Video Courtesy: National Geographic Channel")
import streamlit as st

st.title('Ini adalah tulisan TITLE st.title() :smile: :smile:')
st.header('Ini adalah HEADER st.header() :icecream: 🙆‍♂️')
st.subheader('Ini adalah Subheader st.subheader() 🍌')
st.caption('Ini adalah TULISAN –CAPTION– st.caption()')
st.text('Ini adalah tulisan dari text DENGAN FORMAT st.text()')

col1, col2, col3, col4 = st.columns(4)
col1.metric("Temperature", "25 °C", "1.2 °C")
col2.metric("Wind", "9 kph", "-8%")
col3.metric("Humidity", "86%", "4%")
col4.metric("Rain", "1.6mm")

import pandas as pd
st.write('Ini adalah tulisan dari write DENGAN FORMAT st.write()')
df= pd.DataFrame({
    'first column': [1,2,3,4,5],
    'second column': [10,20,30,40,50]
})
df


# Gambar
st.write('Elemen media Gambar (bismillah LIDM)')
st.image('timprosperous.png', caption='Tim Prosperous', use_container_width=True)

# Audio
st.write('Elemen media Audio')
audio_file = open('Heihua.mp3', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/mp3')


# Video
st.write('Elemen media Video')
video_file = open('sslangkahkecil.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
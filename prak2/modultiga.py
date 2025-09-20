import streamlit as st
import time

st.write("Starting a long computation...")

# Widget slider untuk atur kecepatan
speed = st.slider("Kecepatan (detik per iterasi)", 0.01, 0.5, 0.1)

# Placeholder untuk teks
latest_iteration = st.empty()
# Progress bar
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(speed)  # pakai nilai dari slider

st.write("...and now we're done!")

import streamlit as st
import time

@st.cache_data
def slow_function(a, b):
    time.sleep(2)  
    return a + b

st.write("Testing cache...")

result1 = slow_function(5, 10)
st.write("First call:", result1)

result2 = slow_function(5, 10)  # tidak dihitung ulang
st.write("Second call (cached):", result2)

result3 = slow_function(7, 3)  # beda input → dihitung ulang
st.write("Different input:", result3)

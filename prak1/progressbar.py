import streamlit as st
import time

# ==================== CACHING ====================
@st.cache_data
def slow_function(x):
    # Simulasi fungsi berat
    time.sleep(2)
    return x ** 2

# Widget input
number = st.number_input("Masukkan angka", min_value=0, value=2, step=1)

# Hasil fungsi cache (tidak ditampilkan berlebihan)
hasil_cache = slow_function(number)

# ==================== SESSION STATE ====================
if "counter" not in st.session_state:
    st.session_state.counter = 0

# Tombol untuk menambah counter
if st.button("Tambah Counter"):
    st.session_state.counter += 1

# Tombol untuk reset counter
if st.button("Reset Counter"):
    st.session_state.counter = 0

# ==================== CALLBACK FUNCTION ====================
def slider_callback():
    # Callback jalan saat slider berubah
    st.session_state.hasil_slider = st.session_state.my_slider * 2

# Inisialisasi hasil_slider di session_state
if "hasil_slider" not in st.session_state:
    st.session_state.hasil_slider = 0

# Widget slider dengan callback
st.slider(
    "Geser slider",
    0,
    10,
    5,
    key="my_slider",
    on_change=slider_callback
)

# Widget tambahan: checkbox
if st.checkbox("Aktifkan opsi tambahan"):
    # contoh logika ketika checkbox dipilih
    st.session_state.counter += 1

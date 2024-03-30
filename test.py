import streamlit as st

st.header('Aplikasi Pejumlahan Bilangan Numerik', divider='rainbow')
st.header('_Streamlit_ is :blue[cool] :sunglasses:')

angka_pertama = st.number_input('masukkan angka pertama')
st.write('The first number is', angka_pertama)

angka_kedua = st.number_input('masukkan angka kedua')
st.write('The second number is', angka_kedua)

Operasi_Matematika = angka_pertama * angka_kedua
st.write(f"angka pertama {angka_pertama} x angka kedua {angka_kedua} = {Operasi_Matematika}")
import streamlit as st
from PIL import Image

Curr = ["Naira", "Pounds"," Dollars", "Euro", "Yen", "Cedis"] 
Conv = [1, 1023, 816, 890, 114, 68]   

def convert (num,initial,final):
    ini_id = Curr.index(initial)
    fin_id = Curr.index(final)

    value1 = Conv[ini_id]
    value2 = Conv[fin_id]
    
    result = num * value1/value2

    return round (result,2)



num = st.number_input("how much are you converting")
initial = st.selectbox("Amount currency", Curr)
final = st.selectbox("conversion currency", Curr)

Amount = convert(num,initial,final) 

if st.button("convert"):
    st.write(Amount)

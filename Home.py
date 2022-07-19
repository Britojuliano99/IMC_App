"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd

st.write("IMC calculator")

st.text_input("Your name", key="name")
st.number_input("Your age", key="age")
st.number_input("Your current weigth ?",key="weight")
st.number_input("Your height?(m)",key="height")


if st.button("Your IMC is:"):
    
    Peso=st.session_state.weight
    Altura=st.session_state.height
    try:
        Imc=Peso/Altura**2
    
        st.write(f"{st.session_state.name} your current IMC is {Imc}")
        if Imc>30:
            st.write("É bom ir para a academia viu...")
    except:
        st.write("Você não disse seu peso nem sua altura ai fica dificil")
if st.button("Mensagem do dia"):
    try:
        st.markdown(f"Você {st.session_state.name} é lindo(a)")
    except:
        st.markdown("Qual é seu nome?")
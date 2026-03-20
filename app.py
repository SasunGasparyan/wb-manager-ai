import streamlit as st
import google.generativeai as genai

# Էջի դիզայնը
st.set_page_config(page_title="Wildberries Expert AI", page_icon="📦")

# ԱՅՍՏԵՂ ՏԵՂԱԴՐԻՐ ՔՈ API KEY-Ը
API_KEY = "AIzaSyC0Ly4nQMxa8F9Eg_-6BGvgrA949mqtM84" 

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Էջի վերնագիրը և նկարագրությունը
st.title("📦 WB Manager Assistant")
st.info("Բարև։ Ես ձեր Wildberries-ի օգնականն եմ։ Հարցրեք ինձ ցանկացած բան մեր աշխատանքի մասին։")

# Հարցի դաշտը
user_question = st.text_input("Գրեք ձեր հարցը այստեղ․")

if st.button("Ստանալ պատասխան"):
    if user_question:
        with st.spinner('Մտածում եմ...'):
            # Այստեղ մենք AI-ին ասում ենք, թե ով է ինքը
            prompt = f"Դու Wildberries-ի փորձագետ ես։ Պատասխանիր հայերենով։ \nՀարց: {user_question}"
            response = model.generate_content(prompt)
            st.success("Պատասխան՝")
            st.write(response.text)
    else:
        st.warning("Խնդրում եմ հարց գրեք։")

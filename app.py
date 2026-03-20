import streamlit as st
import google.generativeai as genai

# Էջի կարգավորումներ
st.set_page_config(page_title="Wildberries Expert AI", page_icon="📦", layout="centered")

# Դիզայն (CSS)
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 10px; background-color: #6c5ce7; color: white; height: 3em; font-size: 18px; }
    .stTextInput>div>div>input { border-radius: 10px; border: 2px solid #6c5ce7; }
    </style>
    """, unsafe_allow_html=True)

# ԱՅՍՏԵՂ ՏԵՂԱԴՐԻՐ ՔՈ API KEY-Ը
API_KEY = "ԱՅՍՏԵՂ_ՓԱԿՑՐՈՒ_ՔՈ_ՍՏԱՑԱԾ_ԿՈԴԸ" 

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# ԳԱՂՏՆԻ ԳԻՏԵԼԻՔՆԵՐԻ ԲԱԶԱ (Քո տրամադրած տեքստը)
KNOWLEDGE_BASE = """
[ԱՅՍՏԵՂ ԵՍ ՆԵՐԱՌԵԼ ԵՄ ՔՈ ՈՂՋ ՏԵՔՍՏԸ` ՎԵՐԱԴԱՐՁԻ ԿԱՆՈՆՆԵՐ, ԲՐԱԿԻ ՏԵՍԱԿՆԵՐ, ՊՎԶ-Ի ՕՐՎԱ ՌԵԺԻՄ ԵՎ ԱՅԼՆ:]
"""

st.title("📦 WB Expert Assistant")
st.write("Բարև։ Ես պատրաստ եմ պատասխանել Wildberries-ի աշխատանքային կանոնների վերաբերյալ ձեր հարցերին։")

# Հարցի դաշտ
user_input = st.text_input("Գրեք ձեր հարցը այստեղ․", placeholder="Օրինակ՝ Ինչպե՞ս ընդունել բրակը")

if st.button("Ստանալ պատասխան"):
    if user_input:
        with st.spinner('Մշակում եմ...'):
            full_prompt = f"""
            Դու Wildberries-ի աշխատանքային կանոնների փորձագետ ես։ 
            Օգտագործիր միայն հետևյալ տվյալները պատասխանելու համար: 
            Եթե տվյալների մեջ պատասխանը չկա, ասա, որ տեղեկությունը բացակայում է։
            
            Տվյալներ: {KNOWLEDGE_BASE}
            
            Հարց: {user_input}
            """
            try:
                response = model.generate_content(full_prompt)
                st.markdown("### 📝 Պատասխան")
                st.write(response.text)
            except Exception as e:
                st.error("Տեղի է ունեցել սխալ։ Ստուգեք API Key-ը։")
    else:
        st.warning("Խնդրում եմ հարց գրեք։")

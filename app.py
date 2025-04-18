
import streamlit as st
from openai import OpenAI
import os

st.set_page_config(page_title="📝 تولیدگر اسناد حقوقی", page_icon="🌸", layout="centered")
st.markdown("""
    <style>
    body {background-color: #fefcfb;}
    .stApp {
        background: linear-gradient(to right, #fdf6f0, #fceae8);
        color: #4a4a4a;
    }
    .stButton > button {
        background-color: #ffccd5;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.5em 1em;
    }
    .stTextInput > div > input {
        border-radius: 10px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌸 تولیدگر هوشمند قرارداد، شکایت‌نامه و اعتراض")
st.markdown("با ورود اطلاعات، به‌صورت خودکار سند حقوقی مورد نظر خود را دریافت کنید.")

doc_type = st.selectbox("نوع سند", ["قرارداد", "شکایت‌نامه", "اعتراض"])

client_name = st.text_input("نام موکل")
opponent_name = st.text_input("نام طرف مقابل")
subject = st.text_input("موضوع")
details = st.text_area("جزئیات و توضیحات")

if st.button("✍️ تولید سند"):
    with st.spinner("در حال تولید سند..."):
        import openai
        openai.api_key = st.secrets["OPENAI_API_KEY"]
        prompt = f"""
        لطفاً یک {doc_type} رسمی به زبان فارسی تولید کن. اطلاعات زیر را در آن لحاظ کن:
        - نام موکل: {client_name}
        - نام طرف مقابل: {opponent_name}
        - موضوع: {subject}
        - جزئیات: {details}
        """
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        st.success("✅ سند با موفقیت تولید شد:")
        st.write(response.choices[0].message.content)

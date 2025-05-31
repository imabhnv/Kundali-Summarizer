
import streamlit as st
from app import getInfo

st.set_page_config(page_title="Jyotish AI", layout="centered")

st.title("🧠 Jyotish AI - Kundali Analyzer")
st.markdown("**Enter birth details to generate Kundali charts and analysis.**")

with st.form("kundali_form"):
    col1, col2 = st.columns(2)
    name = col1.text_input("Full Name", "Akshat Varshney")
    gender = col2.selectbox("Gender", ["male", "female"])
    
    col3, col4, col5 = st.columns(3)
    day = col3.text_input("Day", "04")
    month = col4.text_input("Month", "07")
    year = col5.text_input("Year", "2009")

    col6, col7, col8 = st.columns(3)
    hr = col6.text_input("Hour (24h)", "14")
    min = col7.text_input("Minute", "45")
    sec = col8.text_input("Second", "0")

    place = st.text_input("Birthplace", "Chandausi")

    submitted = st.form_submit_button("🔮 Analyze Kundali")

if submitted:
    with st.spinner("🔭 Fetching charts and analysis..."):
        try:
            data = getInfo(name, gender, hr, min, sec, day, month, year, place)
            st.success("✅ Kundali Analysis Complete!")

            for key, title in {
                "birth_chart": "🌌 Birth Chart",
                "mangaldosh_chart": "🌀 Mangal Dosh",
                "kalsapradosh_chart": "🐍 KalSarpDosh Chart",
                "ascendant_chart": "🪔 Your Ascendant",
                "dasha_chart": "〰️ Dasha Chart",
                "career_chart": "💨 Your career",
                "today_chart": "🤨 Today's Horoscope",
                "numerology_chart": "🔢 Numerology Analysis"
            }.items():
                if data.get(key):
                    st.subheader(title)
                    st.image(data[key], caption=title)
        except Exception as e:
            st.error(f"❌ Error: {e}")

st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:gray;'>🚀 Powered by JyotishAI | Developed by Abhinav ⚡</div>",
    unsafe_allow_html=True
)


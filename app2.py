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

            st.subheader("Kundli Charts")
            st.image(data["birth_chart"], caption="🌌 Birth Chart")
            
            st.subheader("Mangal Dosh")
            st.image(data["mangaldosh_chart"], caption="🌀 Mangal Dosh")
            
            st.subheader("Kalsarp Dosh")
            st.image(data["kalsapradosh_chart"], caption="🐍 KalSarpDosh Chart")
            
            st.subheader("Your Ascendant")
            st.image(data["ascendant_chart"], caption="🪔 Your Ascendant")
            
            st.subheader("Dasha Analysis")
            st.image(data["dasha_chart"], caption="〰️ Dasha Chart")
            
            st.subheader("Your Finance, Career and Occupation")
            st.image(data["career_chart"], caption="💨 Your career")
            
            st.subheader("Today's Horoscope")
            st.image(data["today_chart"], caption="🤨 Today's Horoscope")
        except Exception as e:
            st.error(f"❌ Error: {e}")
            
st.write(" ")
st.markdown("---")

footer = """
<style>
.footer {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    width: 100%;
    background-color: #0e1117;
    color: white;
    text-align: center;
    padding: 10px;
    font-size: 14px;
    opacity: 0.85;
    z-index: 100;
}
</style>
<div class="footer">
    🚀 Powered by JyotishAI | Developed by Abhinav ⚡
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
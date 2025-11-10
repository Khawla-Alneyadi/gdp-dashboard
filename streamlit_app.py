streamlit run app.py

import streamlit as st
from datetime import datetime
import time

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Climate Vision Dashboard",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
body {
    background-color: #0e1117;
    font-family: 'Inter', sans-serif;
}
.navbar {
    position: fixed;
    top: 0;
    width: 100%;
    background: rgba(20, 24, 33, 0.8);
    padding: 0.8rem 2rem;
    z-index: 100;
    display: flex;
    justify-content: space-between;
    align-items: center;
    backdrop-filter: blur(10px);
}
.navbar h1 {
    color: #fff;
    font-size: 1.4rem;
    letter-spacing: 1px;
}
.nav-links a {
    color: #ddd;
    margin: 0 1rem;
    text-decoration: none;
    font-weight: 500;
}
.nav-links a:hover {
    color: #4FC3F7;
}
.hero {
    background-image: url('https://i.imgur.com/9TzdG6Q.jpeg');
    background-size: cover;
    background-position: center;
    height: 100vh;
    color: white;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    background-attachment: fixed;
}
.hero h1 {
    font-size: 3.5rem;
    font-weight: 700;
    text-shadow: 0px 0px 15px rgba(0,0,0,0.5);
}
.hero p {
    font-size: 1.2rem;
    color: #e0e0e0;
}
.btn {
    background-color: #0288d1;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 12px 28px;
    margin: 10px;
    font-weight: 600;
    font-size: 1rem;
    cursor: pointer;
    transition: 0.3s;
}
.btn:hover {
    background-color: #039be5;
}
.card {
    background: rgba(25, 30, 40, 0.7);
    border-radius: 15px;
    padding: 25px;
    color: white;
    text-align: center;
    backdrop-filter: blur(10px);
}
.metric-box {
    background: rgba(30, 36, 50, 0.7);
    border-radius: 10px;
    padding: 20px;
    margin: 10px;
    color: #eee;
}
.footer {
    text-align: center;
    color: #aaa;
    font-size: 0.9rem;
    margin-top: 3rem;
    padding: 1rem;
}
</style>
""", unsafe_allow_html=True)

# --- NAVBAR ---
st.markdown("""
<div class="navbar">
    <h1>🌍 Climate Vision</h1>
    <div class="nav-links">
        <a href="#home">Home</a>
        <a href="#explore">Explore Data</a>
        <a href="#change">Change Detection</a>
        <a href="#about">About</a>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br><br>", unsafe_allow_html=True)

# --- PAGE SELECTOR ---
page = st.sidebar.radio("", ["Home", "Explore Data", "Change Detection", "About"], index=0)

# --- HOME PAGE ---
if page == "Home":
    st.markdown("""
    <div class="hero" id="home">
        <h1>Dynamic Climate Vision</h1>
        <p>AI-powered satellite imagery analysis for monitoring land cover and climate change — inspired by Dynamic World.</p>
        <div>
            <a href="#explore"><button class="btn">Explore the Data</button></a>
            <a href="#change"><button class="btn">Discover Change</button></a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🌐 Key Features")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: st.markdown('<div class="card">🌎 **Global Scale**<br>High coverage from Sentinel-2 imagery.</div>', unsafe_allow_html=True)
    with col2: st.markdown('<div class="card">🤖 **AI Powered**<br>Machine learning classification for land cover.</div>', unsafe_allow_html=True)
    with col3: st.markdown('<div class="card">🕒 **Near Realtime**<br>Dynamic updates on environmental change.</div>', unsafe_allow_html=True)
    with col4: st.markdown('<div class="card">📊 **10m Resolution**<br>High accuracy for vegetation, water, and soil.</div>', unsafe_allow_html=True)
    with col5: st.markdown('<div class="card">🌱 **Open Data**<br>Freely available and peer-reviewed datasets.</div>', unsafe_allow_html=True)

# --- EXPLORE DATA PAGE ---
elif page == "Explore Data":
    st.header("🎥 Explore Data: Video Time-Lapse Mode")
    st.markdown("Visualize environmental changes across years using satellite imagery.")

    start, end = st.columns(2)
    with start:
        st.date_input("Start Date", datetime(2015, 1, 1))
    with end:
        st.date_input("End Date", datetime(2024, 12, 31))

    st.slider("Speed", 0.5, 4.0, 1.0, step=0.5)
    st.image("https://i.imgur.com/1jFaWbF.png", caption="Dynamic World Time-lapse Visualization", use_container_width=True)
    play = st.button("▶️ Play")
    if play:
        for i in range(0, 101, 10):
            st.progress(i)
            time.sleep(0.05)
        st.success("Animation Complete ✅")

# --- CHANGE DETECTION PAGE ---
elif page == "Change Detection":
    st.header("📊 Change Detection and Analysis")
    st.markdown("Compare two different years of land cover classification and detect major environmental transformations.")

    before, after = st.columns(2)
    with before:
        st.image("https://i.imgur.com/hZ3N3Ih.png", caption="Before (2018)", use_container_width=True)
    with after:
        st.image("https://i.imgur.com/bd2XoDd.png", caption="After (2024)", use_container_width=True)

    st.markdown("### 🔍 Change Analysis Summary")
    st.markdown("""
    <div class="metric-box">
    <b>Overall Change:</b> +12.8%<br>
    <b>Time Span:</b> 5 years<br>
    <b>Primary Change:</b> Urban Expansion +8.7%<br>
    <b>Forest Cover:</b> -12.3%<br>
    <b>Water Bodies:</b> -3.2%<br>
    <b>Temperature:</b> +1.6°C<br>
    <b>Vegetation Density:</b> -7.8%<br>
    <b>Desert Areas:</b> +5.4%
    </div>
    """, unsafe_allow_html=True)

# --- ABOUT PAGE ---
elif page == "About":
    st.header("ℹ️ About Climate Vision")
    st.markdown("""
    **Climate Vision** is a static demo inspired by **Dynamic World (Google & World Resources Institute)**,
    built with **Streamlit** to illustrate how AI can visualize environmental changes using satellite imagery.

    **Features:**
    - Inspired by *Dynamic World*’s near-real-time land cover data.
    - Designed for environmental awareness and visualization.
    - Built with open tools (Streamlit + CSS + static imagery placeholders).

    **Credits:**
    - 🌍 Imagery Source: Sentinel-2, Dynamic World examples  
    - 🧠 Design: Dynamic World UI inspiration  
    - 🛠️ Developed with: Streamlit and Python  
    """)

st.markdown("<div class='footer'>© 2025 Climate Vision | Inspired by Dynamic World | Built for Educational Use</div>", unsafe_allow_html=True)

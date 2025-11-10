import streamlit as st
from datetime import datetime
import base64
import time

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Dynamic Climate Vision", page_icon="🌍", layout="wide")

# ---- BACKGROUND IMAGE ----
def set_bg(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    bg_css = f"""
    <style>
    body {{
        background-image: url("data:image/webp;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        background-repeat: no-repeat;
        font-family: 'Inter', sans-serif;
        color: white;
    }}
    .block-container {{
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }}
    .hero {{
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        background: rgba(0, 0, 0, 0.55);
        backdrop-filter: blur(4px);
    }}
    h1 {{
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-shadow: 0 0 25px rgba(0,0,0,0.7);
    }}
    p {{
        font-size: 1.1rem;
        max-width: 800px;
        color: #eaeaea;
        margin-bottom: 2rem;
    }}
    .btn {{
        background-color: #0288d1;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.8rem 1.8rem;
        margin: 0.3rem;
        font-weight: 600;
        font-size: 1rem;
        cursor: pointer;
        transition: 0.3s;
    }}
    .btn:hover {{
        background-color: #039be5;
    }}
    .navbar {{
        position: fixed;
        top: 0; left: 0;
        width: 100%;
        background: rgba(10, 15, 25, 0.65);
        backdrop-filter: blur(10px);
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.8rem 2rem;
        z-index: 100;
    }}
    .navbar a {{
        color: #e0e0e0;
        margin-left: 1.5rem;
        text-decoration: none;
        font-weight: 500;
    }}
    .navbar a:hover {{
        color: #4FC3F7;
    }}
    </style>
    """
    st.markdown(bg_css, unsafe_allow_html=True)

set_bg("land_image.webp")

# ---- NAVBAR ----
st.markdown("""
<div class="navbar">
  <div><b>🌍 Dynamic Climate Vision</b></div>
  <div>
    <a href="#home">Home</a>
    <a href="#explore">Explore Data</a>
    <a href="#change">Change Detection</a>
    <a href="#about">About</a>
  </div>
</div>
""", unsafe_allow_html=True)

# ---- SIDEBAR HIDE ----
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {display: none;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# ---- PAGE NAVIGATION ----
page = st.session_state.get("page", "Home")

menu = ["Home", "Explore Data", "Change Detection", "About"]
choice = st.selectbox("", menu, index=menu.index(page), key="menu")

# ---- HOME ----
if choice == "Home":
    st.markdown("""
    <div class="hero" id="home">
        <h1>Dynamic Climate Vision</h1>
        <p>A modern AI-powered platform for exploring environmental change through
        high-resolution satellite imagery — inspired by Google’s Dynamic World.</p>
        <div>
            <a href="#explore"><button class="btn">Explore the Data</button></a>
            <a href="#change"><button class="btn">Discover Change</button></a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---- EXPLORE DATA ----
elif choice == "Explore Data":
    st.markdown("""
    <div class="hero" id="explore">
        <h1>Explore Data</h1>
        <p>Visualize environmental transformations across time using satellite-based
        time-lapse imagery. Adjust your timeline and speed to uncover Earth’s evolving patterns.</p>
        <div><button class="btn">▶️ Play Time-lapse</button></div>
    </div>
    """, unsafe_allow_html=True)

    st.slider("Playback Speed (x)", 0.5, 4.0, 1.0, step=0.5)
    st.date_input("Start Date", datetime(2018, 1, 1))
    st.date_input("End Date", datetime(2024, 12, 31))
    st.image("https://earthengine.google.com/static/images/ee-logo.png",
             caption="Satellite Time-lapse Placeholder", use_container_width=True)

# ---- CHANGE DETECTION ----
elif choice == "Change Detection":
    st.markdown("""
    <div class="hero" id="change">
        <h1>Change Detection</h1>
        <p>Compare two distinct years of satellite classification maps to detect key environmental changes such as deforestation, flooding, or desert expansion.</p>
        <div><button class="btn">Compare Years</button></div>
    </div>
    """, unsafe_allow_html=True)

    before, after = st.columns(2)
    with before:
        st.image("https://i.imgur.com/hZ3N3Ih.png", caption="Before (2018)", use_container_width=True)
    with after:
        st.image("https://i.imgur.com/bd2XoDd.png", caption="After (2024)", use_container_width=True)

    st.markdown("""
    **Detailed Change Summary**
    - Forest Cover: −12.3 %  
    - Urban Expansion: +8.7 %  
    - Water Bodies: −3.2 %  
    - Vegetation Density: −7.8 %  
    - Temperature Increase: +1.6 °C  
    """)

# ---- ABOUT ----
elif choice == "About":
    st.markdown("""
    <div class="hero" id="about">
        <h1>About This Dashboard</h1>
        <p>This dashboard is inspired by Dynamic World by Google & WRI. It showcases the use of
        AI and remote sensing to visualize environmental changes in a clean, modern interface.</p>
        <div><button class="btn">Learn More</button></div>
    </div>
    """, unsafe_allow_html=True)


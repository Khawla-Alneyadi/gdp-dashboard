import streamlit as st
from datetime import datetime
import time
import base64

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Dynamic Climate Vision",
    page_icon="🌍",
    layout="wide",
)

# ---- LOAD BACKGROUND ----
def set_bg(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    page_bg = f"""
    <style>
    body {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        background-repeat: no-repeat;
        color: white;
        font-family: 'Inter', sans-serif;
    }}
    .hero {{
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background: rgba(0,0,0,0.55);
        text-align: center;
        padding: 2rem;
        border-radius: 0;
    }}
    h1 {{
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-shadow: 0 0 20px rgba(0,0,0,0.6);
    }}
    p {{
        font-size: 1.2rem;
        max-width: 800px;
        color: #eaeaea;
        margin-bottom: 2rem;
        line-height: 1.6;
    }}
    .btn-row button {{
        background: #0288d1;
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
    .btn-row button:hover {{
        background: #039be5;
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
        padding: 0.7rem 2rem;
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
    st.markdown(page_bg, unsafe_allow_html=True)

set_bg("land_image.webp")   # <-- make sure this file is in same directory

# ---- NAVBAR ----
st.markdown("""
<div class="navbar">
  <div><b>🌍 Climate Vision</b></div>
  <div>
    <a href="#home">Home</a>
    <a href="#explore">Explore Data</a>
    <a href="#change">Change Detection</a>
    <a href="#about">About</a>
  </div>
</div>
""", unsafe_allow_html=True)
st.markdown("<br><br><br>", unsafe_allow_html=True)

# ---- PAGE SELECTOR ----
page = st.sidebar.radio("", ["Home", "Explore Data", "Change Detection", "About"], index=0)

# ---- HOME ----
if page == "Home":
    st.markdown("""
    <div class="hero" id="home">
      <h1>Dynamic Climate Vision</h1>
      <p>
        A modern AI-powered platform for exploring environmental change through
        high-resolution satellite imagery. Inspired by Google's Dynamic World.
      </p>
      <div class="btn-row">
        <button onclick="window.location.href='#explore'">Explore the Data</button>
        <button onclick="window.location.href='#change'">Discover Change</button>
      </div>
    </div>
    """, unsafe_allow_html=True)

# ---- EXPLORE DATA ----
elif page == "Explore Data":
    st.markdown("""
    <div class="hero" id="explore">
      <h1>Explore Data</h1>
      <p>
        Visualize environmental dynamics over time with satellite-based time-lapse imagery.
        Adjust speed, date range, and discover how landscapes transform.
      </p>
      <div class="btn-row">
        <button>▶️ Play Time-lapse</button>
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.slider("Playback Speed (x)", 0.5, 4.0, 1.0, step=0.5)
    st.date_input("Start Date", datetime(2018,1,1))
    st.date_input("End Date", datetime(2024,12,31))
    st.image("https://earthengine.google.com/static/images/ee-logo.png",
             caption="Satellite Time-lapse Placeholder", use_container_width=True)

# ---- CHANGE DETECTION ----
elif page == "Change Detection":
    st.markdown("""
    <div class="hero" id="change">
      <h1>Change Detection Analysis</h1>
      <p>
        Compare land-cover classifications between two years to detect environmental transitions
        such as deforestation, urbanization, or water-body shifts.
      </p>
      <div class="btn-row">
        <button>Compare Years</button>
      </div>
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
elif page == "About":
    st.markdown("""
    <div class="hero" id="about">
      <h1>About Climate Vision</h1>
      <p>
        This demo mirrors the aesthetics of Dynamic World by Google & WRI, created for
        educational purposes. Built entirely with Streamlit, CSS styling, and static imagery.
      </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    **Credits**
    - Imagery: Sentinel-2, Dynamic World examples  
    - Design Inspiration: Dynamic World  
    - Framework: Streamlit ( Python )  
    - Developer: Khawla Al Neyadi  
    """)


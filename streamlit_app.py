import streamlit as st
from datetime import datetime
import base64
import time

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Climate Analysis", layout="wide")

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
        backdrop-filter: blur(5px);
    }}
    h1 {{
        font-size: 3.5rem;
        font-weight: 700;
        text-shadow: 0 0 25px rgba(0,0,0,0.7);
    }}
    p {{
        font-size: 1.1rem;
        max-width: 800px;
        color: #eaeaea;
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
        transition: 0.3s;
    }}
    .navbar a:hover {{
        color: #4FC3F7;
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
    .side-panel {{
        background: rgba(15, 20, 30, 0.7);
        border-radius: 12px;
        padding: 1.5rem;
        color: white;
        height: 80vh;
    }}
    .side-panel h3 {{
        margin-bottom: 1rem;
        color: #81D4FA;
    }}
    .timeline {{
        margin-top: 1.5rem;
    }}
    </style>
    """
    st.markdown(bg_css, unsafe_allow_html=True)

set_bg("land_image.webp")

# ---- NAVBAR ----
st.markdown("""
<div class="navbar">
  <div><b>Climate Analysis</b></div>
  <div>
    <a href="?page=home">Home</a>
    <a href="?page=explore">Explore Data</a>
    <a href="?page=change">Change Detection</a>
    <a href="?page=about">About</a>
  </div>
</div>
""", unsafe_allow_html=True)
st.markdown("<br><br><br>", unsafe_allow_html=True)

# ---- URL NAVIGATION HANDLING ----
query_params = st.experimental_get_query_params()
page = query_params.get("page", ["home"])[0]

# ---- HOME ----
if page == "home":
    st.markdown("<div class='hero'>", unsafe_allow_html=True)
    st.markdown("<h1>Climate Analysis Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<p>Explore environmental layers and visualize historical satellite imagery across years.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([1.2, 3])

    with col1:
        st.markdown("<div class='side-panel'>", unsafe_allow_html=True)
        st.markdown("<h3>🌍 Data Layers</h3>", unsafe_allow_html=True)
        layers = [
            "Mountains", "Forest", "Vegetation", "Flood", "Desert",
            "Urban", "Sea", "Temperature", "Soil Moisture", "Water"
        ]
        selected_layers = []
        for layer in layers:
            if st.checkbox(layer, value=layer in ["Forest", "Water", "Temperature"]):
                selected_layers.append(layer)

        st.markdown("<div class='timeline'>", unsafe_allow_html=True)
        year = st.slider("Select Year", 2000, 2025, 2012)
        st.markdown(f"**Selected Year:** {year}")
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.image("https://eoimages.gsfc.nasa.gov/images/imagerecords/74000/74418/world.topo.bathy.200412.3x5400x2700.jpg",
                 caption=f"Satellite Imagery for {year}", use_container_width=True)

# ---- EXPLORE DATA ----
elif page == "explore":
    st.markdown("<div class='hero'>", unsafe_allow_html=True)
    st.markdown("<h1>Explore Data</h1>", unsafe_allow_html=True)
    st.markdown("<p>Visualize environmental transformations across time using satellite-based time-lapse imagery.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.slider("Playback Speed (x)", 0.5, 4.0, 1.0, step=0.5)
    st.date_input("Start Date", datetime(2018, 1, 1))
    st.date_input("End Date", datetime(2024, 12, 31))
    st.image("https://earthengine.google.com/static/images/ee-logo.png", caption="Time-lapse Simulation", use_container_width=True)

# ---- CHANGE DETECTION ----
elif page == "change":
    st.markdown("<div class='hero'>", unsafe_allow_html=True)
    st.markdown("<h1>Change Detection</h1>", unsafe_allow_html=True)
    st.markdown("<p>Compare two time periods to detect environmental changes using AI-powered analysis.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    before, after = st.columns(2)
    with before:
        st.image("https://i.imgur.com/hZ3N3Ih.png", caption="Before (2018)", use_container_width=True)
    with after:
        st.image("https://i.imgur.com/bd2XoDd.png", caption="After (2024)", use_container_width=True)

    st.markdown("**Change Summary:**")
    st.write("""
    - Forest Cover: −12.3 %  
    - Urban Expansion: +8.7 %  
    - Water Bodies: −3.2 %  
    - Vegetation Density: −7.8 %  
    - Temperature Increase: +1.6 °C  
    """)

# ---- ABOUT ----
elif page == "about":
    st.markdown("<div class='hero'>", unsafe_allow_html=True)
    st.markdown("<h1>About Climate Analysis</h1>", unsafe_allow_html=True)
    st.markdown("<p>This dashboard visualizes environmental changes inspired by Dynamic World using AI-driven satellite imagery and modern web design.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


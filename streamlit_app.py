import streamlit as st
from datetime import datetime
import base64
import time

# --- CONFIG ---
st.set_page_config(page_title="Climate Analysis", layout="wide")

# --- BACKGROUND IMAGE ---
def set_background(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    css = f"""
    <style>
    body {{
        background-image: url("data:image/webp;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        background-repeat: no-repeat;
        color: white;
        font-family: 'Inter', sans-serif;
    }}
    .block-container {{
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }}
    .navbar {{
        position: fixed;
        top: 0; left: 0;
        width: 100%;
        background: rgba(15, 20, 30, 0.7);
        backdrop-filter: blur(8px);
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 2rem;
        z-index: 100;
    }}
    .navbar a {{
        color: #f0f0f0;
        margin-left: 1.5rem;
        text-decoration: none;
        font-weight: 500;
        transition: 0.3s;
    }}
    .navbar a:hover {{
        color: #4FC3F7;
    }}
    .hero {{
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background: rgba(0, 0, 0, 0.55);
        text-align: center;
        padding: 4rem 2rem;
    }}
    h1 {{
        font-size: 4rem;
        font-weight: 700;
        text-shadow: 0 0 25px rgba(0,0,0,0.7);
    }}
    p {{
        font-size: 1.2rem;
        color: #eaeaea;
        max-width: 800px;
        line-height: 1.6;
        margin-bottom: 2rem;
    }}
    .feature-row {{
        display: flex;
        justify-content: center;
        gap: 2rem;
        flex-wrap: wrap;
        margin-top: 2rem;
    }}
    .feature {{
        background: rgba(30, 35, 50, 0.6);
        border-radius: 10px;
        padding: 1rem 1.5rem;
        min-width: 180px;
        text-align: center;
        font-size: 0.95rem;
        color: #b0e0ff;
    }}
    .btn {{
        background-color: #0288d1;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 0.9rem 1.8rem;
        margin: 0.3rem;
        font-weight: 600;
        cursor: pointer;
        transition: 0.3s;
    }}
    .btn:hover {{
        background-color: #039be5;
    }}
    .panel {{
        background: rgba(15, 20, 30, 0.75);
        border-radius: 12px;
        padding: 2rem;
        margin-top: 2rem;
    }}
    .title-small {{
        color: #81D4FA;
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }}
    footer {{
        text-align: center;
        color: #aaa;
        margin-top: 3rem;
        padding: 1rem;
        font-size: 0.9rem;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

set_background("land_image.webp")

# --- NAVIGATION BAR ---
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

# --- URL NAVIGATION HANDLER ---
query_params = st.experimental_get_query_params()
page = query_params.get("page", ["home"])[0].lower()

# -----------------------------
# 🌍 HOME PAGE
# -----------------------------
if page == "home":
    st.markdown("""
    <div class="hero">
      <h1>Climate Analysis</h1>
      <p>AI-powered satellite-based environmental monitoring system — providing insight into
      how our planet evolves over time with data-driven change detection and visualization.</p>
      <div class="feature-row">
        <div class="feature">🛰️ 10M RESOLUTION</div>
        <div class="feature">🌎 GLOBAL SCALE</div>
        <div class="feature">🤖 AI POWERED</div>
        <div class="feature">⚡ NEAR REALTIME</div>
        <div class="feature">📂 OPEN DATA</div>
      </div>
      <div style="margin-top:2rem;">
        <a href='?page=explore'><button class='btn'>Explore the Data</button></a>
        <a href='?page=change'><button class='btn'>Discover Change</button></a>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # --- Environmental Layers Section ---
    st.markdown("<div class='panel'>", unsafe_allow_html=True)
    st.markdown("<div class='title-small'>Environmental Layers</div>", unsafe_allow_html=True)
    layers = [
        "Mountains", "Forest", "Vegetation", "Flood", "Desert",
        "Urban", "Sea", "Temperature", "Soil Moisture", "Water"
    ]
    cols = st.columns(5)
    for i, layer in enumerate(layers):
        with cols[i % 5]:
            st.checkbox(layer, value=layer in ["Forest", "Water", "Temperature"])

    # --- Timeline Slider ---
    st.markdown("<div class='title-small'>Timeline</div>", unsafe_allow_html=True)
    year = st.slider("Select Year", 2000, 2025, 2012)
    st.image(
        "https://eoimages.gsfc.nasa.gov/images/imagerecords/74000/74418/world.topo.bathy.200412.3x5400x2700.jpg",
        caption=f"Satellite Imagery View — {year}", use_container_width=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# 🎥 EXPLORE DATA PAGE
# -----------------------------
elif page == "explore":
    st.markdown("""
    <div class="hero">
      <h1>Explore Data</h1>
      <p>Visualize environmental transformations over time through satellite-based time-lapse imagery.
      Adjust speed, select date ranges, and discover long-term patterns.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='panel'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.date_input("Start Date", datetime(2018, 1, 1))
    with col2:
        st.date_input("End Date", datetime(2024, 12, 31))
    speed = st.radio("Playback Speed", ["0.5x", "1x", "2x", "4x"], index=1)
    st.markdown(f"**Selected speed:** {speed}")
    st.image("https://earthengine.google.com/static/images/ee-logo.png",
             caption="Simulated Time-lapse View", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# 🔍 CHANGE DETECTION PAGE
# -----------------------------
elif page == "change":
    st.markdown("""
    <div class="hero">
      <h1>Change Detection</h1>
      <p>Compare satellite images between two different time periods to detect environmental
      changes — including deforestation, flooding, and urban expansion.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='panel'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://i.imgur.com/hZ3N3Ih.png", caption="Before (2018)", use_container_width=True)
    with col2:
        st.image("https://i.imgur.com/bd2XoDd.png", caption="After (2024)", use_container_width=True)

    st.markdown("<div class='title-small'>Change Analysis Summary</div>", unsafe_allow_html=True)
    col3, col4, col5 = st.columns(3)
    col3.metric("Forest Cover", "-12.3 %")
    col4.metric("Urban Expansion", "+8.7 %")
    col5.metric("Temperature", "+1.6 °C")

    st.markdown("""
    **Detailed Summary**
    - Water Bodies: −3.2 %  
    - Vegetation Density: −7.8 %  
    - Desert Areas: +5.4 %  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# ℹ️ ABOUT PAGE
# -----------------------------
elif page == "about":
    st.markdown("""
    <div class="hero">
      <h1>About Climate Analysis</h1>
      <p>Climate Analysis is an AI-driven web dashboard inspired by Dynamic World.
      It visualizes satellite imagery and highlights climate-related transformations
      to support research, sustainability, and awareness.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='panel'>", unsafe_allow_html=True)
    st.write("""
    **Features:**
    - 🌎 Global satellite imagery analysis  
    - 🤖 AI models for environmental classification  
    - 🕒 Timeline tracking for land-cover change  
    - 📊 Interactive visualization and reports  

    **Data Sources:**
    - Sentinel-2, MODIS, VIIRS, Landsat  
    - Dynamic World Dataset (Google & WRI)  

    **Developed by:** Khawla Alneyadi (UAE University)  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<footer>© 2025 Climate Analysis | Built with Streamlit | Inspired by Dynamic World</footer>", unsafe_allow_html=True)

  

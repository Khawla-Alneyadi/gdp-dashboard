import streamlit as st
import time
from datetime import datetime

# ----- PAGE CONFIG -----
st.set_page_config(
    page_title="Climate Analysis Dashboard",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----- GLOBAL STYLE -----
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: #fafafa;
    }
    .main {
        background-color: #0e1117;
        color: white;
    }
    .stButton>button {
        background-color: #1E88E5;
        color: white;
        border-radius: 8px;
        height: 40px;
        width: 180px;
        border: none;
        font-weight: 500;
    }
    .stButton>button:hover {
        background-color: #1565C0;
        color: #fff;
    }
    .metric-card {
        background-color: #1b1f2a;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ----- NAVIGATION -----
page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home Dashboard", "🎥 Video Time-lapse", "📊 Change Detection"],
)

# ----- SIDEBAR FILTERS -----
st.sidebar.header("Data Layers")
layers = [
    "Mountains", "Forest", "Vegetation", "Flood", "Desert",
    "Urban", "Sea", "Temperature", "Soil Moisture", "Water"
]
selected_layers = [layer for layer in layers if st.sidebar.checkbox(layer, value=True)]

# ----- PAGE 1: HOME -----
if page == "🏠 Home Dashboard":
    st.title("🌍 Climate & Environmental Monitoring Dashboard")
    st.markdown("### Explore satellite-based environmental data and historical imagery")

    col1, col2 = st.columns([3, 1])
    with col1:
        st.image("https://eoimages.gsfc.nasa.gov/images/imagerecords/74000/74418/world.topo.bathy.200412.3x5400x2700.jpg",
                 caption="Global Earth Visualization", use_container_width=True)
    with col2:
        st.markdown("#### Quick Controls")
        st.slider("Zoom Level (%)", 50, 150, 100)
        year = st.slider("Select Year", 2000, 2025, 2012)
        st.markdown(f"**Selected Year:** {year}")

        st.write("**Navigate to:**")
        video_btn = st.button("🎞️ Video Mode")
        change_btn = st.button("📊 Change Detection")

        if video_btn:
            st.session_state.page = "🎥 Video Time-lapse"
            st.experimental_rerun()
        if change_btn:
            st.session_state.page = "📊 Change Detection"
            st.experimental_rerun()

    st.markdown("---")
    st.markdown("**Selected Layers:** " + ", ".join(selected_layers))
    st.markdown("Historical imagery timeline below:")
    st.slider("Timeline", 2000, 2025, 2012, step=1)

# ----- PAGE 2: VIDEO MODE -----
elif page == "🎥 Video Time-lapse":
    st.title("🎥 Video Time-Lapse Mode")
    st.markdown("Watch environmental changes over time through animated satellite imagery.")

    st.markdown("#### Configuration")
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2020, 1, 1))
    with col2:
        end_date = st.date_input("End Date", datetime(2030, 12, 31))

    speed = st.radio("Playback Speed", ["0.5x", "1x", "2x", "4x"], index=1)
    st.markdown(f"**Speed Selected:** {speed}")

    st.image("https://eoimages.gsfc.nasa.gov/images/imagerecords/74000/74418/world.topo.bathy.200412.3x5400x2700.jpg",
             caption="Animated time-lapse (example)", use_container_width=True)
    st.progress(0)
    progress_bar = st.progress(0)
    play = st.button("▶️ Play")

    if play:
        for i in range(101):
            time.sleep(0.02)
            progress_bar.progress(i)
        st.success("Playback Complete ✅")

    st.markdown("⬅️ [Back to Dashboard](#)")

# ----- PAGE 3: CHANGE DETECTION -----
elif page == "📊 Change Detection":
    st.title("📊 Environmental Change Detection Analysis")
    st.markdown("Compare two time periods to detect environmental changes and generate an analysis summary.")

    col1, col2 = st.columns(2)
    with col1:
        st.image("https://eoimages.gsfc.nasa.gov/images/imagerecords/74000/74418/world.topo.bathy.200412.3x5400x2700.jpg",
                 caption="Before (2020)", use_container_width=True)
    with col2:
        st.image("https://eoimages.gsfc.nasa.gov/images/imagerecords/57000/57730/world.topo.bathy.200412.3x5400x2700.jpg",
                 caption="After (2024)", use_container_width=True)

    st.markdown("### 🔍 Change Analysis Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Overall Change", "12.8%", "Significant increase detected")
    col2.metric("Time Span", "5 years")
    col3.metric("Primary Change", "Vegetation +4.2%")

    st.markdown("#### Detailed Analysis")
    st.markdown("""
        <div class="metric-card">
            <b>Forest Cover:</b> -12.3%<br>
            <b>Urban Expansion:</b> +8.7%<br>
            <b>Water Bodies:</b> -3.2%<br>
            <b>Temperature:</b> +1.6°C<br>
            <b>Vegetation Density:</b> -7.8%<br>
            <b>Desert Areas:</b> +5.4%
        </div>
    """, unsafe_allow_html=True)

    st.markdown("⬅️ [Back to Dashboard](#)")


import streamlit as st

# Title of the app
st.title("Titik Lokasi Wisata di Edinburg")

# Path to your HTML file
html_file_path = "edinburgh_poi_map.html"

# Read the HTML content
with open(html_file_path, "r", encoding="utf-8") as file:
    html_content = file.read()

# Display the HTML content using Streamlit
st.components.v1.html(html_content, height=600, scrolling=True)
st.markdown("Terlihat bahwa di edinburgh tempat wisata terbanyak adalah Struktur bangunan yang ditandai oleh titik dengan warna oranye")
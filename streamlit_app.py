import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="My First Web Page", layout="wide")

try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_data = f.read()
    
    # Display the HTML content
    components.html(html_data, height=800, scrolling=True)
except FileNotFoundError:
    st.error("The file index.html was not found.")
except Exception as e:
    st.error(f"An error occurred: {e}")

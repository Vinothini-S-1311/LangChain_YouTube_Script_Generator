import streamlit as st
from script_generator import generate_script

st.title("🎬 YouTube Script Generator")
user_input = st.text_input("Enter a topic for your video")

if user_input:
    script = generate_script(user_input)
    st.subheader("Generated Script:")
    st.write(script)
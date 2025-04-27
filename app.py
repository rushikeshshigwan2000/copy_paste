import pyperclip
import streamlit as st

# App title
st.title("Clipboard Manager - Copy from Anywhere & Paste Anywhere")

# Instructions
st.write("Copy text from anywhere (browser, Word, etc.) and paste it here.")

# Button to copy from clipboard
if st.button("Copy from Clipboard"):
    # Get current clipboard content
    clipboard_data = pyperclip.paste()
    if clipboard_data.strip():
        st.success(f"Copied: {clipboard_data}")
    else:
        st.error("Clipboard is empty. Copy something first!")

# Textbox to display pasted content
pasted_data = st.text_area("Pasted Content", value="", height=150)

# Button to paste into the text area
if st.button("Paste into Text Area"):
    if pasted_data.strip():
        pyperclip.copy(pasted_data)  # Copy the pasted data back to clipboard
        st.success("Data has been pasted into the text area and copied back to clipboard!")
    else:
        st.error("Please paste something into the text area first.")

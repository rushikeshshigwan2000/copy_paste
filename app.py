import streamlit as st
import pandas as pd
import pyperclip
import os

# Initialize a list to store copied items
copied_items = []

# App title
st.title("Clipboard-to-Excel Paster")

# Instructions
st.write("Copy multiple items from anywhere (browser, Word, etc.).")

# Step 1: Input file path
file_path = st.text_input("Enter Excel file path (e.g., C:/path/to/your_file.xlsx)")

# Check if the path exists
if file_path:
    if not os.path.exists(file_path):
        st.error("File does not exist. Please check the path.")
    else:
        # Read the existing Excel file
        df = pd.read_excel(file_path)

        # Display existing data in the Excel file (optional)
        st.write("Existing data in the file:")
        st.write(df)

# Button to copy data
if st.button("Copy from Clipboard"):
    # Read current clipboard content
    clipboard_data = pyperclip.paste()
    if clipboard_data.strip():
        copied_items.append(clipboard_data.strip())
        st.success(f"Copied: {clipboard_data}")
    else:
        st.error("Clipboard is empty. Copy something first!")

# Show copied items (for feedback)
st.write("Items copied so far:")
st.write(copied_items)

# Button to save copied data to Excel
if st.button("Paste to Excel"):
    if not copied_items:
        st.error("No items copied yet!")
    elif not file_path:
        st.error("Please enter an Excel file path.")
    else:
        try:
            # Convert copied items to horizontal format (single row)
            row_data = copied_items

            # Append copied data as a new row
            df = pd.concat([df, pd.DataFrame([row_data])], ignore_index=True)

            # Save the updated Excel file
            df.to_excel(file_path, index=False)

            # Clear copied items after saving
            copied_items.clear()
            st.success(f"Data pasted and saved to {file_path}!")

        except Exception as e:
            st.error(f"Error: {e}")

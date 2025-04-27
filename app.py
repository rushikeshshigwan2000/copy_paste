# better_streamlit_paste_tool.py

import streamlit as st
import pandas as pd
import pyperclip
import os

st.set_page_config(page_title="Smart Paster", page_icon="📋")

st.title("Smart Excel Paster 📋➡️📄")

# Step 1: Select or open Excel file
file_path = st.text_input("Enter Excel file path (or leave default 'output.xlsx'):", value="output.xlsx")

# Step 2: Choose columns
columns = st.multiselect("Select the columns to paste into:", 
                         options=["Name", "Position", "Department", "Location", "Email", "Phone"])

# Step 3: Paste Button
if st.button("Paste from Clipboard"):
    if not columns:
        st.warning("Please select columns first.")
    else:
        try:
            pasted_text = pyperclip.paste()

            if not pasted_text.strip():
                st.error("Clipboard is empty. Copy something first!")
            else:
                # Try to split pasted content (by new lines)
                pasted_items = pasted_text.strip().split("\n")
                
                if len(pasted_items) != len(columns):
                    st.error(f"Mismatch: You selected {len(columns)} columns but copied {len(pasted_items)} items.")
                else:
                    # Open a modal to preview
                    with st.modal("Confirm Pasted Data"):
                        st.write("Here is what you copied:")

                        preview = {col: val for col, val in zip(columns, pasted_items)}
                        st.table(preview.items())

                        if st.button("Confirm and Save"):
                            # Load or create Excel
                            if os.path.exists(file_path):
                                df = pd.read_excel(file_path)
                            else:
                                df = pd.DataFrame(columns=columns)

                            # Add new row
                            df = pd.concat([df, pd.DataFrame([preview])], ignore_index=True)

                            # Save Excel
                            df.to_excel(file_path, index=False)
                            st.success(f"Row saved successfully to {file_path}!")

        except Exception as e:
            st.error(f"Error: {e}")


import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# 1. .env se API Key load karein
load_dotenv()

# 2. Gemini ko configure karein
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# 3. Model define karein (YEH LINE MISSING THI)
model = genai.GenerativeModel("gemini-1.5-flash")

# 4. Function banayein
def my_output(query):
    # Ab yahan 'model' kaam karega
    response = model.generate_content(query)
    return response.text

# 5. UI Development using Streamlit
st.set_page_config(page_title="QUERY_BOT")
st.header("QUERY_BOT")

# Input field
input_text = st.text_input("Input: ", key="input")
submit = st.button("Ask your query")

# Button click hone par action
if submit:
    if input_text:
        try:
            response = my_output(input_text)
            st.subheader("The Response is:")
            st.write(response)
        except Exception as e:
            st.error(f"Error aa gaya: {e}")
    else:
        st.warning("Please enter a query first!")
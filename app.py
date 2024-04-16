from openai import OpenAI
import streamlit as st

# Read the API key from a file
with open("D:\A Internship JAN 2024\BACKEND_SESSIONS\GENAI_APPS\genai_app_2\key\.openai_key1.txt") as f:
    key = f.read().strip()

# Initialize OpenAI client
client = OpenAI(api_key=key)

# Set page title and background
st.set_page_config(page_title="AI Code Reviewer", page_icon=":rainbow:", layout="wide")
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;  /* Light gray background */
    }
    .stApp {
        max-width: 800px;  /* Limit app width */
        margin: 0 auto;  /* Center align content */
    }
    .stButton>button {
        background-color: #4a90e2;  /* Blue button */
        color: #ffffff;  /* White text */
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;  /* Rounded text input */
        border: 2px solid #4a90e2;  /* Blue border */
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.title("AI Code Reviewer")
st.write("Welcome to the AI Code Reviewer! Enter your Python code below and click 'Review' to get started.")

# User input
prompt = st.text_area("Enter your Python code...", height=200)

# Review button
if st.button("Review"):
    # Generate response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=[
            {'role': 'system', 'content': "You are a helpful AI Assistant. Given Python code, you always review the code and find out the bugs. Below are the bugs found and the corrected code."},
            {'role': 'user', 'content': prompt}
        ]
    )
    
    # Display response
    st.subheader("Bugs found:")
    st.write(response.choices[0].message['content'])  # Display bugs found
    st.subheader("Corrected code:")
    st.code(response.choices[1].message['content'], language='python')  # Display corrected code

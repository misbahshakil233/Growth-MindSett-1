import streamlit as st
import pandas as pd
import os
from datetime import datetime

# File path for storing user data
CSV_FILE = "progress_journal.csv"

# Create CSV file if not exists
def initialize_csv():
    if not os.path.exists(CSV_FILE):
        df = pd.DataFrame(columns=["Name", "Goal", "Bio", "Interests", "Email", "Effort", "Learning", "Reflection", "Date"])
        df.to_csv(CSV_FILE, index=False)

# Load user data
def load_data():
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    return pd.DataFrame(columns=["Name", "Goal", "Bio", "Interests", "Email", "Effort", "Learning", "Reflection", "Date"])

# Save user data
def save_data(user_data):
    df = load_data()
    df = pd.concat([df, pd.DataFrame([user_data])], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)

# UI Styling
dark_mode = st.toggle("🌙 Dark Mode", value=True)

st.markdown(
    f"""
    <style>
    body {{ background: {'#121212' if dark_mode else '#f5f5f5'}; }}
    .main-container {{ background: {'#1e1e1e' if dark_mode else 'white'}; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); }}
    h1, h2, h3, p {{ color: {'#ffffff' if dark_mode else '#333333'}; text-align: center; }}
    .stButton button {{ background: linear-gradient(135deg, #ff00ff, #007bff); color: white; border: none; border-radius: 8px; padding: 10px 20px; font-size: 16px; font-weight: bold; }}
    .stButton button:hover {{ background: linear-gradient(135deg, #007bff, #ff00ff); }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("📖 Personal Progress Journal")
st.subheader("Track your learning, efforts & reflections effortlessly! 🌱")

# User Input Form
with st.container():
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    name = st.text_input("Enter your name")
    goal = st.text_input("Your learning goal")
    bio = st.text_area("Write a short bio")
    interests = st.text_input("Your interests")
    email = st.text_input("Your email (optional)")
    
    effort = st.slider("Effort Level (1-10)", 1, 10, 5)
    learning = st.slider("Learning Progress (1-10)", 1, 10, 5)
    reflection = st.text_area("Weekly Reflection")
    
    if st.button("💾 Save Entry"):
        user_data = {
            "Name": name, "Goal": goal, "Bio": bio, "Interests": interests,
            "Email": email, "Effort": effort, "Learning": learning,
            "Reflection": reflection, "Date": datetime.now().strftime("%Y-%m-%d")
        }
        save_data(user_data)
        st.success("✅ Entry Saved Successfully!")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Display Saved Entries
data = load_data()
if not data.empty:
    st.subheader("📊 Your Learning Progress")
    st.dataframe(data)

# Initialize CSV file
initialize_csv()
import re
import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Regex Extractor Hub", page_icon="✨", layout="wide")

# --- Header ---
st.markdown("<h1 style='text-align: center;'>✨ Regex Extractor Hub ✨</h1>", unsafe_allow_html=True)
st.write("Easily extract patterns from text with Regex and learn how they work!")

# --- Sidebar Menu ---
st.sidebar.header("🛠 Choose an Extractor")
option = st.sidebar.radio(
    "Select a Regex Tool:",
    ["Hashtag Extractor", "Email Username Extractor", "Book Title Extractor", "Date Extractor"]
)

# --- Function to show explanation in a styled card ---
def show_result(title, text, pattern, match_info, explanation):
    with st.container():
        st.subheader(title)
        col1, col2 = st.columns([2, 1])

        with col1:
            st.text_area("Your Input:", value=text, height=100)
            st.code(pattern, language="regex")

            if match_info:
                st.success(match_info)
            else:
                st.warning("No match found!")

        with col2:
            st.markdown("### 🔎 Regex Breakdown")
            st.markdown(explanation)

# --- Extractors ---
if option == "Hashtag Extractor":
    text = st.text_input("Enter a Tweet:", "AI is amazing! #MachineLearning #AI #DataScience")
    pattern = r"#(\w+)"
    matches = re.findall(pattern, text)
    show_result(
        "📌 Hashtag Extractor",
        text,
        pattern,
        f"Extracted hashtags: {matches}" if matches else None,
        """
        - `#` → finds the hashtag symbol  
        - `(\\w+)` → captures one or more word characters (the hashtag text)
        """
    )

elif option == "Email Username Extractor":
    text = st.text_input("Enter an Email ID:", "student123@mit.edu")
    pattern = r"^([a-zA-Z0-9._%+-]+)@"
    match = re.search(pattern, text)
    show_result(
        "📧 Email Username Extractor",
        text,
        pattern,
        f"Extracted username: {match.group(1)}" if match else None,
        """
        - `^` → start of string  
        - `([a-zA-Z0-9._%+-]+)` → captures valid username characters  
        - `@` → stops capturing before '@'
        """
    )

elif option == "Book Title Extractor":
    text = st.text_input("Enter a Sentence:", "I recently read 'The Alchemist' by Paulo Coelho.")
    pattern = r"'([^']+)'"
    match = re.search(pattern, text)
    show_result(
        "📚 Book Title Extractor",
        text,
        pattern,
        f"Extracted book title: {match.group(1)}" if match else None,
        """
        - `'` → looks for starting single quote  
        - `([^']+)` → captures all characters until the next `'`  
        - `'` → ending single quote
        """
    )

elif option == "Date Extractor":
    text = st.text_input("Enter a Sentence:", "The meeting is scheduled on 21-08-2025 at 10 AM.")
    pattern = r"\d{2}-\d{2}-\d{4}"
    match = re.search(pattern, text)
    show_result(
        "📅 Date Extractor",
        text,
        pattern,
        f"Extracted date: {match.group()}" if match else None,
        """
        - `\\d{2}` → 2 digits (day or month)  
        - `-` → dash separator  
        - `\\d{4}` → 4 digits (year)
        """
    )

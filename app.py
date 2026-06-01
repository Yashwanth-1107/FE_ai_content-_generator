import streamlit as st
import requests

BACKEND_URL = st.secrets["be_server_url"]

st.set_page_config(
    page_title="AI Content Generator",
    layout="wide"
)

st.title("🚀 AI Content Generator")

st.write("Generate Blogs, LinkedIn Posts, Captions, Emails and more")

topic = st.text_input(
    "Enter Topic"
)

technology = st.selectbox(
    "Select Technology",
    [
        "Python",
        "React",
        "MERN",
        "NodeJS",
        "FastAPI",
        "AI",
        "GenAI"
    ]
)

content_type = st.selectbox(
    "Content Type",
    [
        "LinkedIn Post",
        "Blog",
        "Instagram Caption",
        "Twitter Post",
        "Email",
        "YouTube Description"
    ]
)

tone = st.selectbox(
    "Tone",
    [
        "Professional",
        "Technical",
        "Friendly",
        "Casual",
        "Marketing"
    ]
)

generate = st.button("Generate Content")


if generate:

    if not topic:
        st.warning("Please enter a topic")
        st.stop()

    with st.spinner("Generating Content..."):

        try:
            # ✅ FIX: use JSON instead of params
            response = requests.post(
                f"{BACKEND_URL}/generate",
                json={
                    "topic": topic,
                    "technology": technology,
                    "content_type": content_type,
                    "tone": tone
                },
                timeout=120
            )

            st.write("Status Code:", response.status_code)

            # Try parsing safely
            try:
                data = response.json()
            except Exception:
                st.error("Invalid JSON response from backend")
                st.write(response.text)
                st.stop()

            # Handle success
            if response.status_code == 200 and "content" in data:
                st.success("Content Generated Successfully")
                st.subheader("Generated Content")
                st.write(data["content"])

            # Handle backend error
            else:
                st.error("Backend Error")
                st.write(data)

        except requests.exceptions.RequestException as e:
            st.error("Connection Error")
            st.write(str(e))
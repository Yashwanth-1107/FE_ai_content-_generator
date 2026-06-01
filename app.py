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

    if topic == "":
        st.warning("Please enter topic")
    else:

        with st.spinner("Generating Content..."):

            response = requests.post(
                f"{BACKEND_URL}/generate",
                params={
                    "topic": topic,
                    "technology": technology,
                    "content_type": content_type,
                    "tone": tone
                }
            )

            # result = response.json()
            st.write("Status Code:", response.status_code)
            st.write("Response Text:", response.json()["content"])

            st.success("Content Generated Successfully")

            st.subheader("Generated Content")

           
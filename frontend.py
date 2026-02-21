import streamlit as st
import requests

# Point to your FastAPI endpoint
BACKEND_URL = "http://127.0.0.1:8000/analyze-and-search/"

st.set_page_config(page_title="AI Career Matcher", page_icon="💼")

st.title("🚀 AI-Powered Career Assistant")
st.markdown("Upload your resume to get AI-driven job matches and live listings.")

# Sidebar for location setting
with st.sidebar:
    st.header("Search Settings")
    location = st.text_input("Preferred Location", value="Remote")
    st.info("Uses Llama 3 for analysis and Adzuna for live job links.")

# File Uploader
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type="pdf")

if uploaded_file is not None:
    if st.button("Analyze My Career"):
        with st.spinner("Parsing resume and consulting AI..."):
            try:
                # Prepare the file for the POST request
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
                params = {"location": location}

                response = requests.post(BACKEND_URL, files=files, params=params)

                if response.status_code == 200:
                    result = response.json()

                    # 1. Display AI Reasoning
                    st.success("Analysis Complete!")
                    st.subheader("💡 AI Recommendations & Reasoning")
                    st.write(result.get("candidate_analysis"))

                    # 2. Display Live Job Matches
                    st.divider()
                    st.subheader("🔗 Live Job Opportunities")

                    jobs = result.get("top_matches", [])
                    if jobs:
                        for job in jobs:
                            # Display each job in a nice "Card" style
                            with st.container(border=True):
                                col1, col2 = st.columns([3, 1])
                                with col1:
                                    st.markdown(f"**{job['title']}**")
                                    st.caption(f"{job['company']} • {job['location']}")
                                with col2:
                                    st.link_button("View Job", job['link'])
                    else:
                        st.warning("No live jobs found for these titles in your location.")

                else:
                    st.error(f"Backend error: {response.text}")

            except Exception as e:
                st.error(f"Could not connect to backend: {e}")
🚀 Getting Started
# 1. Prerequisites

Python 3.10+

Ollama installed and running with Llama3 (ollama run llama3)

An Adzuna API Key

# 2. Installation

## Clone the repository
    git clone https://github.com/Johanz211/Resume-Analyser.git
    cd Resume-Analyser

## Install dependencies
    pip install -r requirements.txt

# 3. Running the Application

You will need two terminal windows open:
    
Terminal 1: Start the Backend (Uvicorn)
    
    uvicorn app.main:app --port 8080

Terminal 2: Start the Frontend (Streamlit)
    
    streamlit run main.py --server.port 8501

💡 How it Works
Upload: Drop your resume (PDF) into the Streamlit interface.
    
Extract: The backend sends the raw text to Llama3 (localhost:11434) to identify your top skills and job titles.
    
Search: Those keywords are passed to the Adzuna API to find matching vacancies.
    
Result: View a curated list of job links directly in your browser.
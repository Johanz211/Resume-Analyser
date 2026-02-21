from fastapi import FastAPI, File, UploadFile
from backend import llm_request
from backend import adzuna_helper
from backend import parse_pdf  # Import your new helper file

app = FastAPI(title="Resume Matcher")

@app.post("/analyze-and-search/")
async def analyze_and_search(file: UploadFile = File(...), location: str = "Remote"):
    # 1. Use the method from your parse_pdf.py file
    text = await parse_pdf.parse_pdf(file)

    # 2. Get Structured AI Opinion
    ai_output = llm_request.get_llm_opinion(text)
    reasoning = ai_output.get("reasoning")
    suggested_titles = ai_output.get("job_titles")

    # 3. Fetch Real Jobs based on AI titles
    live_jobs = adzuna_helper.search_adzuna_jobs(suggested_titles, location)

    return {
        "candidate_analysis": reasoning,
        "top_matches": live_jobs
    }
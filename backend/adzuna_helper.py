import requests
import os

def get_secret(key):
    backend_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(backend_dir)
    secret_path = os.path.join(project_root, "Secrets", "adzuna.properties")
    try:
        with open(secret_path, "r") as f:
            for line in f:
                if line.startswith(key):
                    return line.split("=")[1].strip().strip('"').strip("'")
    except FileNotFoundError:
        print(f"Error: {secret_path} not found.")
    return None


APP_ID = get_secret("APP_ID") #Your app id here
APP_KEY = get_secret("APP_KEY") #Your api key from adzuna
COUNTRY = "in"  # Use 'us', 'uk', 'in', etc.


def search_adzuna_jobs(job_titles, location="Remote"):
    all_jobs = []
    print(APP_ID)
    print(job_titles)
    # We search for the first few titles suggested by the AI
    for title in job_titles:
        url = f"https://api.adzuna.com/v1/api/jobs/{COUNTRY}/search/1"
        params = {
            "app_id": APP_ID,
            "app_key": APP_KEY,
            "results_per_page": 5,
            "what": title,
            "where": location,
            "content-type": "application/json"
        }

        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                results = response.json().get("results", [])
                for job in results:
                    all_jobs.append({
                        "title": job.get("title"),
                        "company": job.get("company", {}).get("display_name"),
                        "link": job.get("redirect_url"),
                        "location": job.get("location", {}).get("display_name")
                    })
        except Exception as e:
            print(f"Adzuna Error: {e}")

    return all_jobs


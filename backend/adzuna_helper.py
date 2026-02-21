import requests

APP_ID = "123132" #Your app id here
APP_KEY = "1313hh213123" #Your api key from adzuna
COUNTRY = "in"  # Use 'us', 'uk', 'in', etc.


def search_adzuna_jobs(job_titles, location="Remote"):
    all_jobs = []

    # We search for the first few titles suggested by the AI
    for title in job_titles[:2]:
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
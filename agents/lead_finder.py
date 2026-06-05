import os
import requests
from dotenv import load_dotenv

load_dotenv()


class LeadFinder:

    BLACKLIST_DOMAINS = [
        "wikipedia.org",
        "fibre2fashion.com",
        "indiamart.com",
        "justdial.com",
        "tradeindia.com",
        "linkedin.com",
        "facebook.com",
        "instagram.com",
        "youtube.com",
        "twitter.com",
        "x.com"
        "scribd.com"
    ]

    def __init__(self):
        self.api_key = os.getenv("SERPER_API_KEY")

    def search_companies(self, query, num_results=10):

        try:

            url = "https://google.serper.dev/search"

            payload = {
                "q": query,
                "num": num_results
            }

            headers = {
                "X-API-KEY": self.api_key,
                "Content-Type": "application/json"
            }

            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=30
            )

            response.raise_for_status()

            data = response.json()

            companies = []

            for result in data.get("organic", []):

                website = result.get("link", "")

                # Skip unwanted domains
                if any(
                    domain in website.lower()
                    for domain in self.BLACKLIST_DOMAINS
                ):
                    continue

                companies.append(
                    {
                        "title": result.get("title", ""),
                        "website": website,
                        "snippet": result.get("snippet", "")
                    }
                )

            return companies

        except Exception as e:

            print(f"Lead Finder Error: {e}")

            return []
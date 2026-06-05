from firecrawl import FirecrawlApp
from dotenv import load_dotenv
import os

load_dotenv()


class WebsiteExtractor:

    def __init__(self):
        self.app = FirecrawlApp(
            api_key=os.getenv("FIRECRAWL_API_KEY")
        )

    def extract_company_info(self, website_url):

        try:

            result = self.app.extract(
                urls=[website_url],
                prompt="""
                Extract business information from this company website.

                Return ONLY structured JSON in the following format:

                {
                    "company_name": "",
                    "industry": "",
                    "products": [],
                    "services": [],
                    "email": "",
                    "phone": "",
                    "address": "",
                    "website": "",
                    "about_company": ""
                }

                Rules:
                - Extract all available products.
                - Extract all available services.
                - Extract business email if available.
                - Extract phone number if available.
                - Extract company address if available.
                - Keep about_company under 100 words.
                - Return empty string ("") if information is unavailable.
                - Return only valid JSON.
                """
            )

            return result

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }
from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


class LeadAnalyzer:

    def analyze_company(self, company_data):

        prompt = f"""
        You are an expert business analyst.

        Analyze the following company data:

        {company_data}

        Return ONLY valid JSON in the following format:

        {{
            "lead_score": 0,
            "company_summary": "",
            "strengths": [],
            "opportunities": [],
            "recommendation": ""
        }}

        Rules:
        - lead_score must be between 0 and 100
        - Return only JSON
        - Do not include markdown
        - Do not include explanations outside JSON
        """

        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3,
                max_tokens=1000
            )

            response_text = response.choices[0].message.content

            # Remove markdown code blocks if present
            response_text = (
                response_text
                .replace("```json", "")
                .replace("```", "")
                .strip()
            )

            try:
                return json.loads(response_text)

            except json.JSONDecodeError:
                return {
                    "error": "Invalid JSON returned by model",
                    "raw_response": response_text
                }

        except Exception as e:
            return {
                "error": str(e)
            }
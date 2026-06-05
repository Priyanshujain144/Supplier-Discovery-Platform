from agents.analyzer import LeadAnalyzer

sample_data = {
    "companyName": "Zoho Corporation",
    "industry": "Cloud Software",
    "products": [
        "CRM",
        "Books",
        "Desk"
    ]
}

analyzer = LeadAnalyzer()

result = analyzer.analyze_company(sample_data)

print(result)
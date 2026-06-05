from agents.extractor import WebsiteExtractor

extractor = WebsiteExtractor()

result = extractor.extract_company_info(
    "https://www.zoho.com"
)

if hasattr(result, "success") and result.success:
    print(result.data)
else:
    print(result)
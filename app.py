from agents.extractor import WebsiteExtractor
from agents.analyzer import LeadAnalyzer

def main():

    website = input("Enter Company Website URL: ")

    extractor = WebsiteExtractor()
    analyzer = LeadAnalyzer()

    print("\nExtracting company information...\n")

    extracted_data = extractor.extract_company_info(
        website
    )

    if not extracted_data.success:
        print("Extraction Failed!")
        return

    print("Extraction Complete!\n")

    company_data = extracted_data.data

    print("Company Data:")
    print(company_data)

    print("\nAnalyzing Company...\n")

    analysis = analyzer.analyze_company(
        company_data
    )

    print("\n========== ANALYSIS REPORT ==========\n")

    print(f"Lead Score: {analysis['lead_score']}")
    print(f"\nSummary:\n{analysis['company_summary']}")

    print("\nStrengths:")
    for strength in analysis["strengths"]:
        print(f"- {strength}")

    print("\nOpportunities:")
    for opportunity in analysis["opportunities"]:
        print(f"- {opportunity}")

    print(
        f"\nRecommendation:\n{analysis['recommendation']}"
    )

if __name__ == "__main__":
    main()
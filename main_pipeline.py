from agents.lead_finder import LeadFinder
from agents.extractor import WebsiteExtractor

finder = LeadFinder()
extractor = WebsiteExtractor()

query = input("Enter Search Query: ")

search_query = f"{query} manufacturer official website"

companies = finder.search_companies(
    search_query,
    num_results=5
)

results = []

for company in companies:

    print(f"\nExtracting: {company['website']}")

    try:

        extracted = extractor.extract_company_info(
            company["website"]
        )

        if extracted.success:

            results.append(
                extracted.data
            )

    except Exception as e:

        print("Error:", e)

print("\n\nSUPPLIER RESULTS\n")

for idx, supplier in enumerate(results, start=1):

    print("=" * 60)

    print(
        f"Supplier {idx}: "
        f"{supplier.get('company_name')}"
    )

    print(
        f"Industry: "
        f"{supplier.get('industry')}"
    )

    print(
        f"Products: "
        f"{supplier.get('products')}"
    )

    print(
        f"Email: "
        f"{supplier.get('email')}"
    )

    print(
        f"Phone: "
        f"{supplier.get('phone')}"
    )

    print(
        f"Website: "
        f"{supplier.get('website')}"
    )
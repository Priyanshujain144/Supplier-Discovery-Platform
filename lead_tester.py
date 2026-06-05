from agents.lead_finder import LeadFinder

finder = LeadFinder()

results = finder.search_companies(
    "cloth manufacturers in surat",
    num_results=10
)

for i, company in enumerate(results, start=1):

    print(f"\nCompany {i}")

    print("Title:", company["title"])
    print("Website:", company["website"])
    print("Snippet:", company["snippet"])
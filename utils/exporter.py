import pandas as pd


def create_dataframe(results):

    cleaned_data = []

    for supplier in results:

        cleaned_data.append({
            "Company": supplier.get("company_name", ""),
            "Industry": supplier.get("industry", ""),
            "Email": supplier.get("email", ""),
            "Phone": supplier.get("phone", ""),
            "Website": supplier.get("website", ""),
            "Products": ", ".join(
                supplier.get("products", [])
            )
        })

    return pd.DataFrame(cleaned_data)
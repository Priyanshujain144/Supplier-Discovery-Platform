import streamlit as st
import pandas as pd

from agents.lead_finder import LeadFinder
from agents.extractor import WebsiteExtractor
from utils.exporter import create_dataframe


st.set_page_config(
    page_title="AI Supplier Discovery Agent",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 AI Supplier Discovery Agent")

st.markdown(
    """
    Search manufacturers, suppliers, and businesses.
    """
)

query = st.text_input(
    "Search Query",
    placeholder="garment manufacturers in delhi"
)

num_results = st.slider(
    "Number of Websites to Search",
    5,
    20,
    10
)

if st.button("Search Suppliers"):

    finder = LeadFinder()
    extractor = WebsiteExtractor()

    results = []

    progress = st.progress(0)

    with st.spinner("Finding suppliers..."):

        companies = finder.search_companies(
            query,
            num_results=num_results
        )

        total = len(companies)

        for idx, company in enumerate(companies):

            try:

                extracted = (
                    extractor.extract_company_info(
                        company["website"]
                    )
                )

                if extracted.success:

                    results.append(
                        extracted.data
                    )

            except Exception:
                pass

            progress.progress(
                (idx + 1) / total
            )

    st.success(
        f"Found {len(results)} suppliers"
    )

    # Metrics

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Suppliers Found",
            len(results)
        )

    with col2:
        st.metric(
            "Websites Processed",
            len(companies)
        )

    with col3:
        st.metric(
            "Success Rate",
            f"{round(len(results)/max(len(companies),1)*100)}%"
        )

    # DataFrame

    df = create_dataframe(results)

    st.subheader("Supplier Database")

    st.dataframe(
        df,
        use_container_width=True
    )

    # CSV Download

    csv = df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name="supplier_results.csv",
        mime="text/csv"
    )

    # Expandable Details

    st.subheader("Supplier Details")

    for supplier in results:

        with st.expander(
            supplier.get(
                "company_name",
                "Unknown Company"
            )
        ):

            st.write(
                "**Industry:**",
                supplier.get("industry")
            )

            st.write(
                "**Website:**",
                supplier.get("website")
            )

            st.write(
                "**Email:**",
                supplier.get("email")
            )

            st.write(
                "**Phone:**",
                supplier.get("phone")
            )

            st.write(
                "**Products:**"
            )

            st.write(
                supplier.get("products")
            )

            st.write(
                "**About Company:**"
            )

            st.write(
                supplier.get(
                    "about_company"
                )
            )
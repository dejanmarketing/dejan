# authority_usage_streamlit.py

import streamlit as st
from dejan import get_authority

def main():
    st.title("Domain Authority Checker")
    st.write("Enter a domain to check its authority score using Dejan's Authority Metric.")

    # Input for the domain
    domain = st.text_input("Domain", "dejanmarketing.com")

    if st.button("Check Authority"):
        try:
            # Fetch the authority metric
            authority = get_authority(domain)
            st.success(f"Domain Authority for {domain}: {authority:.2f}")
        except ValueError as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()

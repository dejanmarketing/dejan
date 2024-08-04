import streamlit as st
from dejan import linkbert

def main():
    # Set up the Streamlit app title and description
    st.title("LinkBERT Token Prediction")
    st.write("This app uses the LinkBERT model to predict link tokens in the provided text.")
    
    # Initialize the LinkBERTInference model
    model = linkbert.LinkBERTInference()

    # Input text area
    text = st.text_area("Enter text to analyze", "LinkBERT is a model developed by Dejan Marketing designed to predict natural link placement within web content.")

    # Grouping strategy selection
    group = st.selectbox(
        "Select the grouping strategy",
        options=["subtoken", "token", "phrase"],
        index=2  # Default to "token"
    )

    # Button to trigger the prediction
    if st.button("Predict Link Tokens"):
        # Perform prediction based on selected grouping strategy
        links = model.predict_link_tokens(text, group=group)

        # Display the results
        st.write(f"Predicted link tokens ({group}):")
        st.write(links)

if __name__ == "__main__":
    main()

from dejan import linkbert

def main():
    # Initialize the LinkBERTInference model
    model = linkbert.LinkBERTInference()

    # Sample text for prediction
    text = "LinkBERT is a model developed by Dejan Marketing designed to predict natural link placement within web content."

    print("Input Text:")
    print(text)
    print("-" * 50)

    # Group by subtoken
    links_subtoken = model.predict_link_tokens(text, group="subtoken")
    print(f"Predicted link tokens (subtoken): {links_subtoken}")

    # Group by token
    links_token = model.predict_link_tokens(text, group="token")
    print(f"Predicted link tokens (token): {links_token}")

    # Group by phrase
    links_phrase = model.predict_link_tokens(text, group="phrase")
    print(f"Predicted link tokens (phrase): {links_phrase}")

if __name__ == "__main__":
    main()

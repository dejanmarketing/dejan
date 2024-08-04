import click
from dejan import linkbert

@click.command()
@click.option('--text', prompt='Enter text to analyze', help='The text you want to analyze for link predictions.')
@click.option('--group', default='token', help='The grouping strategy to use: subtoken, token, or phrase.')
def main(text, group):
    """CLI tool for LinkBERT Token Prediction"""
    # Initialize the LinkBERTInference model
    model = linkbert.LinkBERTInference()

    # Perform prediction based on selected grouping strategy
    links = model.predict_link_tokens(text, group=group)

    # Display the results in the CLI
    print(f"\nPredicted link tokens ({group}):")
    for link in links:
        print(link)

if __name__ == "__main__":
    main()

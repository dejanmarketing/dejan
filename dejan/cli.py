import click
import subprocess
import os

@click.group()
def cli():
    """Dejan CLI for various tools."""
    pass

@cli.command()
def linkbert():
    """Run the LinkBERT Streamlit app."""
    app_path = os.path.join(os.path.dirname(__file__), 'apps', 'linkbert_app.py')
    subprocess.run(["streamlit", "run", app_path])

if __name__ == "__main__":
    cli()

# Simplified cli.py for testing
import click

@click.group()
def cli():
    pass

@cli.command()
def linkbert():
    click.echo("LinkBERT command executed")

if __name__ == "__main__":
    cli()

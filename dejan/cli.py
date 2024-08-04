import click

@click.group()
def cli():
    """Dejan CLI for various tools."""
    pass

@cli.command()
def linkbert():
    """Run the LinkBERT CLI tool."""
    from dejan.apps.linkbert_app import main
    main()

if __name__ == "__main__":
    cli()

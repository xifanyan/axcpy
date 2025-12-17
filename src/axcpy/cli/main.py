"""Main CLI entry point."""

import typer
from rich.console import Console

app = typer.Typer(
    name="axcpy",
    help="Axcelerate Python Client - CLI for OpenText Axcelerate eDiscovery service",
    no_args_is_help=True,
)

console = Console()


@app.command()
def version() -> None:
    """Show version information."""
    from axcpy.__version__ import __version__

    console.print(f"axcpy version {__version__}")


@app.command()
def config() -> None:
    """Manage configuration."""
    console.print("[yellow]Configuration management coming soon...[/yellow]")


# TODO: Add subcommands for ADP and SearchWebAPI
# from axcpy.cli.adp_commands import adp_app
# from axcpy.cli.search_commands import search_app
# app.add_typer(adp_app, name="adp")
# app.add_typer(search_app, name="search")


if __name__ == "__main__":
    app()

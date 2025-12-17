"""SearchWebAPI CLI commands."""

import typer
from rich.console import Console

search_app = typer.Typer(name="search", help="SearchWebAPI commands")
console = Console()


@search_app.command()
def query(q: str) -> None:
    """Execute search query.

    Args:
        q: Search query string
    """
    console.print(f"[yellow]Executing query: {q}[/yellow]")
    # TODO: Implement query


@search_app.command()
def export() -> None:
    """Export search results."""
    console.print("[yellow]Export coming soon...[/yellow]")

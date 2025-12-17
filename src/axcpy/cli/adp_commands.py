"""ADP CLI commands."""

import typer
from rich.console import Console

adp_app = typer.Typer(name="adp", help="ADP service commands")
console = Console()


@adp_app.command()
def cases() -> None:
    """Manage cases."""
    console.print("[yellow]ADP cases commands coming soon...[/yellow]")


@adp_app.command()
def docs() -> None:
    """Manage documents."""
    console.print("[yellow]ADP documents commands coming soon...[/yellow]")


@adp_app.command()
def search(query: str) -> None:
    """Search documents.

    Args:
        query: Search query string
    """
    console.print(f"[yellow]Searching for: {query}[/yellow]")
    # TODO: Implement search

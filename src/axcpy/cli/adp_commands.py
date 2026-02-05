"""ADP CLI commands."""

import json

import typer
from rich.console import Console
from rich.json import JSON
from rich.table import Table

from axcpy.adp import ADPClient, Session
from axcpy.adp.models import ListEntitiesTaskConfig

adp_app = typer.Typer(name="adp", help="ADP service commands")
console = Console()


@adp_app.command()
def list_entities(
    id: str = typer.Option(..., "--id", "-i", help="Entity ID to list"),
    type: str = typer.Option("singleMindServer", "--type", "-t", help="Entity type"),
    username: str = typer.Option(
        ..., "--username", "-u", help="Authentication username", envvar="ADP_USERNAME"
    ),
    password: str = typer.Option(
        ...,
        "--password",
        "-p",
        help="Authentication password",
        envvar="ADP_PASSWORD",
        hide_input=True,
    ),
    base_url: str = typer.Option(
        ..., "--base-url", "-b", help="ADP service base URL", envvar="ADP_BASE_URL"
    ),
    ignore_tls: bool = typer.Option(
        False, "--ignore-tls", help="Ignore TLS certificate verification"
    ),
    timeout: float = typer.Option(30.0, "--timeout", help="Request timeout in seconds"),
    debug: bool = typer.Option(False, "--debug", help="Enable debug logging"),
) -> None:
    """List entities from ADP service.

    Example:
        axcpy adp list-entities --id singleMindServer.demo00001
    """
    console.print(f"[cyan]Listing entities with ID: {id}[/cyan]")

    try:
        client = ADPClient(
            base_url=base_url,
            ignore_tls=ignore_tls,
            timeout=timeout,
            debug=debug,
        )

        session = Session(
            client=client,
            auth_username=username,
            auth_password=password,
        )

        config = ListEntitiesTaskConfig(
            adp_listEntities_id=id,
            adp_listEntities_type=type,
        )

        result = session.list_entities(config)

        if result.adp_entities_json_output:
            if debug:
                console.print("\n[bold]Debug: First entity fields:[/bold]")
                if result.adp_entities_json_output:
                    console.print(
                        JSON(json.dumps(result.adp_entities_json_output[0], indent=2))
                    )

            table = Table(title="Entities")
            table.add_column("ID", style="cyan")
            table.add_column("Display Name", style="green")
            table.add_column("Status", style="yellow")

            for entity in result.adp_entities_json_output:
                entity_id = entity.get("id", "")
                display_name = entity.get("displayName", "")
                process_status = entity.get("processStatus", "")
                table.add_row(entity_id, display_name, process_status)

            console.print(table)

            console.print(
                f"\n[yellow]Output file:[/yellow] {result.adp_entities_output_file_name}"
            )
            console.print(
                f"[yellow]Total entities:[/yellow] {len(result.adp_entities_json_output)}"
            )

            if debug:
                console.print("\n[bold]Full result:[/bold]")
                console.print(JSON(json.dumps(result.model_dump(), indent=2)))
        else:
            console.print("[yellow]No entities found[/yellow]")

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1)


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

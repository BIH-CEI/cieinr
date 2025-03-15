
import typer

app = typer.Typer()

def version_callback(value: bool):
    """
    Display the RareLink version and exit.
    """
    if value:
        typer.echo("CIEINR version v1.0.0")
        raise typer.Exit()

@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Show the RareLink version and exit.",
    )
):
    """
    Welcome to the CIEINR CLI! This tool is designed to help you setup and 
    manage the CIEINR tooling around the local REDCap site,
    and export the site's phenopackets.
    """
    pass

if __name__ == "__main__":
    app()

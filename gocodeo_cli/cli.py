"""
SaaS-Builder CLI - Generate full-stack SaaS applications with AI.
"""
from importlib.metadata import PackageNotFoundError, version as _package_version

import typer
from rich import print
from rich.console import Console
from rich.panel import Panel

from gocodeo_cli.commands import build

try:
    __version__ = _package_version("saas-builder")
except PackageNotFoundError:  # running from source without an installed package
    __version__ = "0.8"

# Initialize Typer app
app = typer.Typer(
    name="saas-builder",
    help="AI-powered CLI for generating full-stack SaaS applications",
    add_completion=False,
)

# Create console for rich output
console = Console()

def version_callback(value: bool):
    """Print version information."""
    if value:
        print(Panel.fit(
            f"[bold blue]SaaS-Builder[/bold blue] [yellow]v{__version__}[/yellow]",
            title="Version",
            border_style="blue",
        ))
        raise typer.Exit()

@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        "-v",
        help="Show version information.",
        callback=version_callback,
        is_eager=True,
    ),
):
    """
    SaaS-Builder CLI - Generate full-stack SaaS applications with AI.
    """
    pass

app.command()(build.init)

if __name__ == "__main__":
    app() 
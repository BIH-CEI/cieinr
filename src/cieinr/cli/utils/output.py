"""
Output formatting utilities for consistent CLI display.
"""
import typer
import os
from .terminal_utils import between_section_separator

def format_section(title: str):
    """
    Format a section title in the CLI output.
    """
    between_section_separator()
    typer.secho(f"[{title}]", fg=typer.colors.BRIGHT_BLUE, bold=True)

def success_message(message: str):
    """
    Display a success message with a green checkmark.
    """
    typer.secho(f"✅ {message}", fg=typer.colors.GREEN)

def error_message(message: str):
    """
    Display an error message with a red X.
    """
    typer.secho(f"❌ {message}", fg=typer.colors.RED)

def warning_message(message: str):
    """
    Display a warning message with a yellow exclamation mark.
    """
    typer.secho(f"⚠️ {message}", fg=typer.colors.YELLOW)

def info_message(message: str):
    """
    Display an informational message with a blue info symbol.
    """
    typer.secho(f"ℹ️ {message}", fg=typer.colors.BRIGHT_BLUE)

def hyperlink(text: str, url: str) -> str:
    """
    Create a clickable hyperlink for terminal output with a fallback for 
    unsupported terminals.
    """
    if "TERM" in os.environ and os.environ["TERM"] not in ("dumb", ""):
        return f"\033]8;;{url}\033\\{text}\033]8;;\033\\"
    else:
        return f"{text} ({url})"

def format_command(command: str) -> str:
    """
    Format a terminal command to make it stand out.
    """
    return typer.style(command, fg=typer.colors.BRIGHT_CYAN)
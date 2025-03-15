import typer
import json
from pathlib import Path
from typing import Optional
from cieinr.cli.utils.env import set_env_variable, load_env, validate_required_keys
from cieinr.cli.utils.output import (
    format_header, 
    format_section, 
    format_command, 
    success_message, 
    error_message, 
    warning_message, 
    hyperlink
)

app = typer.Typer(help="Setup commands for CIEINR")

API_CONFIG_FILE = Path("cieinr_apiconfig.json")
API_CONFIG_DOWNLOADS = Path.home() / "Downloads" / "cieinr_apiconfig.json"

# Mask input for sensitive data
def mask_input(prompt: str, mask_char: str = "•") -> str:
    """
    Get masked input from the user for sensitive data.
    
    This is a simplified version. In a real implementation, 
    you might want to use a more sophisticated approach for security.
    
    Args:
        prompt (str): The prompt text to show.
        mask_char (str): Character to use for masking.
        
    Returns:
        str: The user's input.
    """
    return typer.prompt(prompt, hide_input=True)

@app.command("keys")
def setup_keys():
    """
    Setup API keys and configuration for CIEINR.
    
    Configures BioPortal API key, REDCap URL, Project ID and API Token,
    and sets the creator name for phenopacket metadata.
    """
    format_header("CIEINR API Setup")
    typer.echo("This setup will guide you through configuring your CIEINR API keys and variables.")
    
    # Load existing environment variables
    env_vars = load_env()
    
    # Step 1: BioPortal API Key
    bioportal_api_token = mask_input(
        "Step 1: Enter your BioPortal API key (input will be masked): ",
    )
    
    # Step 2: REDCap URL
    redcap_url = typer.prompt(
        "Step 2: Enter your REDCap URL (e.g., https://redcap.example.com/api/)",
        default=env_vars.get("REDCAP_URL", ""),
        show_default=bool(env_vars.get("REDCAP_URL", "")),
    )
    
    # Step 3: REDCap project ID and name
    redcap_project_id = typer.prompt(
        "Step 3: Enter your REDCap Project ID",
        default=env_vars.get("REDCAP_PROJECT_ID", ""),
        show_default=bool(env_vars.get("REDCAP_PROJECT_ID", "")),
    )
    
    redcap_project_name = typer.prompt(
        "Step 4: Enter your REDCap Project Name",
        default=env_vars.get("REDCAP_PROJECT_NAME", ""),
        show_default=bool(env_vars.get("REDCAP_PROJECT_NAME", "")),
    )
    
    # Step 4: REDCap API Token
    redcap_api_token = mask_input(
        "Step 5: Enter your REDCap API Token (input will be masked): ",
    )
    
    # Step 5: Created By
    created_by = typer.prompt(
        "Step 6: Enter your name or identifier for the 'Created By' field",
        default=env_vars.get("CREATED_BY", ""),
        show_default=bool(env_vars.get("CREATED_BY", "")),
    )
    
    # Save values to .env file
    set_env_variable("BIOPORTAL_API_TOKEN", bioportal_api_token)
    set_env_variable("REDCAP_URL", redcap_url)
    set_env_variable("REDCAP_PROJECT_ID", redcap_project_id)
    set_env_variable("REDCAP_PROJECT_NAME", f'"{redcap_project_name}"')
    set_env_variable("REDCAP_API_TOKEN", redcap_api_token)
    set_env_variable("CREATED_BY", f'"{created_by}"')
    
    success_message("API keys and configurations have been saved to .env file.")
    
    # Create the JSON configuration file
    config = {
        "bioportal_api_token": bioportal_api_token,
        "redcap-url": redcap_url,
        "id": redcap_project_id,
        "token": redcap_api_token,
    }
    
    try:
        with open(API_CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=4)
        success_message(f"Configuration saved to {API_CONFIG_FILE}.")
    except Exception as e:
        error_message(f"Failed to save JSON configuration file: {e}")
        raise typer.Exit(1)
    
    # Optional: Save to Downloads folder
    save_locally = typer.confirm(
        "Would you like to save this configuration in your Downloads folder as well?"
    )
    if save_locally:
        try:
            with open(API_CONFIG_DOWNLOADS, 'w') as f:
                json.dump(config, f, indent=4)
            success_message(f"Configuration saved to {API_CONFIG_DOWNLOADS}.")
        except Exception as e:
            error_message(f"Failed to save configuration in Downloads: {e}")
    
    # Validate the configuration
    success = validate_required_keys([
        "BIOPORTAL_API_TOKEN", 
        "REDCAP_URL", 
        "REDCAP_PROJECT_ID",
        "REDCAP_API_TOKEN",
        "CREATED_BY"
    ])
    
    if success:
        success_message("Setup complete! Your configuration has been validated.")
        typer.echo(f"Run {format_command('cieinr download records')} to download records from REDCap.")
    else:
        error_message("Setup failed validation. Please check your configuration.")

@app.command("view")
def view_config():
    """View the current CIEINR configuration."""
    format_header("CIEINR Configuration")
    
    # Load environment variables
    env_vars = load_env()
    
    # Display the environment variables
    format_section("Environment Variables")
    for key, value in env_vars.items():
        if key.startswith(("REDCAP_", "BIOPORTAL_", "CREATED_BY")):
            # Mask sensitive values
            if key in ["REDCAP_API_TOKEN", "BIOPORTAL_API_TOKEN"]:
                value_display = value[:4] + "..." if value else ""
            else:
                value_display = value
            typer.echo(f"{key}: {value_display}")
    
    # Display the JSON configuration if it exists
    if API_CONFIG_FILE.exists():
        format_section("API Configuration")
        try:
            with open(API_CONFIG_FILE, 'r') as f:
                config = json.load(f)
                
            # Mask sensitive values
            if "bioportal_api_token" in config:
                config["bioportal_api_token"] = config["bioportal_api_token"][:4] + "..."
            if "token" in config:
                config["token"] = config["token"][:4] + "..."
                
            typer.echo(json.dumps(config, indent=2))
        except Exception as e:
            error_message(f"Failed to read API configuration: {e}")
    else:
        warning_message(f"API configuration file {API_CONFIG_FILE} not found.")
        
    typer.echo(f"\nRun {format_command('cieinr setup keys')} to update your configuration.")

@app.command("reset")
def reset_config():
    """
    Reset the CIEINR configuration, removing API keys and settings.
    """
    format_header("Reset Configuration")
    
    # Confirm reset
    confirm = typer.confirm(
        "This will delete your current CIEINR configuration, including API keys. Continue?",
        abort=True
    )
    
    # Remove .env file if it exists
    env_path = Path(".env")
    if env_path.exists():
        try:
            env_path.unlink()
            success_message(".env file has been removed.")
        except Exception as e:
            error_message(f"Failed to remove .env file: {e}")
    else:
        warning_message("No .env file found.")
    
    # Remove API config file if it exists
    if API_CONFIG_FILE.exists():
        try:
            API_CONFIG_FILE.unlink()
            success_message(f"{API_CONFIG_FILE} has been removed.")
        except Exception as e:
            error_message(f"Failed to remove {API_CONFIG_FILE}: {e}")
    else:
        warning_message(f"No {API_CONFIG_FILE} file found.")
    
    typer.echo(f"Run {format_command('cieinr setup keys')} to set up your configuration again.")
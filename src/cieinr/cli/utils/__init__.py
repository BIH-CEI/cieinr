"""
Bridge module to import utilities from RareLink CLI.

This module imports utilities from the RareLink CLI and re-exports them
for use in the CIEINR CLI. This allows code reuse without duplication.
"""
import sys
import os
from pathlib import Path

# Add the submodules to sys.path to allow importing
submodules_path = Path(__file__).parent.parent.parent.parent.parent / "submodules"
if submodules_path.exists():
    if str(submodules_path) not in sys.path:
        sys.path.append(str(submodules_path))

# Also check the alternate location
submodules_src_path = Path(__file__).parent.parent.parent.parent.parent / "submodules" / "src"
if submodules_src_path.exists():
    if str(submodules_src_path) not in sys.path:
        sys.path.append(str(submodules_src_path))

# Import from RareLink if available, otherwise use stub implementations
try:
    # Import from RareLink utilities
    from rarelink.cli.utils import (
        # Terminal utils
        before_header_separator,
        after_header_separator,
        between_section_separator,
        end_of_section_separator,
        display_progress_bar, 
        confirm_action,
        display_banner,
        masked_input,
        # String utils
        format_command,
        error_text,
        success_text,
        hint_text,
        hyperlink,
        format_header,
        # File utils
        download_file,
        ensure_directory_exists,
        read_json,
        write_json,
        # Pipeline utils
        execute_pipeline,
        validate_pipeline_config,
        log_pipeline_results,
        # Version utils
        get_current_version,
        # Logging utils
        setup_logger,
        log_info,
        log_warning,
        log_error,
        log_exception,
        # Validation utils
        validate_env,
        validate_config,
        validate_url,
        validate_redcap_projects_json,
        # Write utils
        write_env_file
    )
    
    # These may not be in RareLink, so we import from our local modules
    from .env import (
        set_env_variable,
        load_env,
        validate_required_keys,
        get_env_variable
    )
    
    # Output utils may have additional helpers in our version
    from .output import (
        format_section,
        success_message,
        error_message,
        warning_message,
        info_message
    )
    
except ImportError as e:
    print(f"Error importing RareLink utilities: {e}")
    print("Using local implementations for utilities...")
    
    # Fall back to local implementations
    from .terminal_utils import (
        before_header_separator,
        after_header_separator,
        between_section_separator,
        end_of_section_separator,
        display_progress_bar, 
        confirm_action,
        display_banner,
        masked_input,
    )
    from .string_utils import (
        format_command,
        error_text,
        success_text,
        hint_text,
        hyperlink,
        format_header
    )
    from .file_utils import (
        download_file,
        ensure_directory_exists,
        read_json,
        write_json
    )
    from .pipeline_utils import (
        execute_pipeline,
        validate_pipeline_config,
        log_pipeline_results
    )
    from .version_utils import get_current_version
    from .logging_utils import (
        setup_logger,
        log_info,
        log_warning,
        log_error,
        log_exception
    )
    from .validation_utils import (
        validate_env,
        validate_config,
        validate_url,
        validate_redcap_projects_json
    )
    from .write_utils import (
        write_env_file
    )
    from .output import (
        format_section,
        success_message,
        error_message,
        warning_message,
        info_message
    )
    from .env import (
        set_env_variable,
        load_env,
        validate_required_keys,
        get_env_variable
    )

__all__ = [
    # Terminal utils
    "before_header_separator",
    "after_header_separator",
    "between_section_separator",
    "end_of_section_separator",
    "display_progress_bar",
    "confirm_action",
    "display_banner",
    "masked_input",
    # String utils
    "format_command",
    "error_text",
    "success_text",
    "hint_text",
    "hyperlink",
    "format_header",
    # File utils
    "download_file",
    "ensure_directory_exists",
    "read_json",
    "write_json",
    # Pipeline utils
    "execute_pipeline",
    "validate_pipeline_config",
    "log_pipeline_results",
    # Version utils
    "get_current_version",
    # Logging utils
    "setup_logger",
    "log_info",
    "log_warning",
    "log_error",
    "log_exception",
    # validation utils
    "validate_env",
    "validate_config",
    "validate_url",
    "validate_redcap_projects_json",
    # write utils
    "write_env_file",
    # Output utils
    "format_section",
    "success_message",
    "error_message",
    "warning_message",
    "info_message",
    # Environment utils
    "set_env_variable",
    "load_env",
    "validate_required_keys",
    "get_env_variable"
]
"""
Logging utilities for consistent log formatting.
"""
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional, Union

def setup_logger(
    name: str, 
    log_file: Optional[Union[str, Path]] = None,
    level: int = logging.INFO
) -> logging.Logger:
    """
    Set up a logger with consistent formatting.
    
    Args:
        name: Name of the logger
        log_file: Optional file path to write logs to
        level: Logging level
        
    Returns:
        Logger: Configured logger instance
    """
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Remove existing handlers to avoid duplication
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    
    # Format logs consistently
    log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)
    
    # File handler (if specified)
    if log_file:
        # Create directory if it doesn't exist
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)
    
    return logger

def log_info(logger: logging.Logger, message: str) -> None:
    """Log an info message."""
    logger.info(message)

def log_warning(logger: logging.Logger, message: str) -> None:
    """Log a warning message."""
    logger.warning(message)

def log_error(logger: logging.Logger, message: str) -> None:
    """Log an error message."""
    logger.error(message)

def log_exception(logger: logging.Logger, message: str, exc: Exception) -> None:
    """Log an exception with a custom message."""
    logger.exception(f"{message}: {str(exc)}")
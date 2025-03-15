"""
Pipeline utility functions for handling data processing workflows.
"""
import time
import logging
from typing import Dict, Any, Callable, List, Optional
from tqdm import tqdm

def validate_pipeline_config(config: Dict[str, Any], required_keys: List[str]) -> bool:
    """
    Validate that a pipeline configuration contains all required keys.
    
    Args:
        config: Configuration dictionary
        required_keys: List of required keys
        
    Returns:
        bool: True if valid
        
    Raises:
        ValueError: If configuration is invalid
    """
    missing = []
    for key in required_keys:
        if key not in config:
            missing.append(key)
    
    if missing:
        raise ValueError(f"Missing required configuration keys: {', '.join(missing)}")
    
    return True

def execute_pipeline(pipeline_steps: List[Dict[str, Any]], data: Any = None) -> Dict[str, Any]:
    """
    Execute a multi-step pipeline with progress tracking.
    
    Args:
        pipeline_steps: List of dictionaries with 'name', 'function', and 'args' keys
        data: Optional initial data input
        
    Returns:
        Dict: Results from each step
    """
    results = {"input": data}
    
    # Set up logging
    logger = logging.getLogger("pipeline")
    
    # Execute pipeline steps
    for i, step in enumerate(tqdm(pipeline_steps, desc="Pipeline Progress")):
        step_name = step.get("name", f"Step {i+1}")
        step_func = step.get("function")
        step_args = step.get("args", {})
        
        if not callable(step_func):
            raise ValueError(f"Invalid pipeline step function for step: {step_name}")
        
        try:
            logger.info(f"Starting pipeline step: {step_name}")
            start_time = time.time()
            
            # Execute the step
            if data is not None and step.get("pass_input", True):
                step_result = step_func(data, **step_args)
            else:
                step_result = step_func(**step_args)
            
            end_time = time.time()
            duration = end_time - start_time
            
            # Store result
            results[step_name] = step_result
            
            # Update data for the next step if needed
            if step.get("update_input", False):
                data = step_result
            
            logger.info(f"Completed pipeline step: {step_name} in {duration:.2f} seconds")
        except Exception as e:
            logger.error(f"Pipeline step {step_name} failed: {str(e)}")
            results[f"{step_name}_error"] = str(e)
            if step.get("fail_on_error", True):
                raise
    
    return results

def log_pipeline_results(results: Dict[str, Any], 
                        success_callback: Optional[Callable] = None, 
                        error_callback: Optional[Callable] = None) -> None:
    """
    Log the results of a pipeline execution and trigger callbacks.
    
    Args:
        results: Results dictionary from execute_pipeline
        success_callback: Function to call on success
        error_callback: Function to call on error
    """
    logger = logging.getLogger("pipeline")
    
    # Check for errors
    errors = {k: v for k, v in results.items() if k.endswith("_error")}
    
    if errors:
        logger.error(f"Pipeline completed with {len(errors)} errors")
        for step, error in errors.items():
            logger.error(f"  {step}: {error}")
        
        if error_callback:
            error_callback(results, errors)
    else:
        logger.info("Pipeline completed successfully")
        if success_callback:
            success_callback(results)
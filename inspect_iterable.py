def inspect_structure(obj, indent=0):
    """
    Recursively inspects a nested data structure and prints the type,
    shape, and length of each component.

    Args:
        obj: The variable to inspect (e.g., a tuple, list, tensor).
        indent (int): The current indentation level for pretty-printing.
    """
    # Create an indentation string for readability
    indent_str = "  " * indent
    
    # Get the object's type as a string
    obj_type = type(obj).__name__
    
    # Determine size/shape information based on type
    if isinstance(obj, torch.Tensor):
        size_info = f"shape={obj.shape}, dtype={obj.dtype}"
    elif isinstance(obj, np.ndarray):
        size_info = f"shape={obj.shape}, dtype={obj.dtype}"
    elif isinstance(obj, (list, tuple, dict)):
        size_info = f"length={len(obj)}"
    else:
        # For simple data types like int, float, str, just show the value
        size_info = f"value={repr(obj)}"
        
    # Print the information for the current object
    print(f"{indent_str}- {obj_type} ({size_info})")
    
    # --- Recurse into iterable elements ---
    if isinstance(obj, (list, tuple)):
        for item in obj:
            inspect_structure(item, indent=indent + 1)
    elif isinstance(obj, dict):
        for key, value in obj.items():
            # Print the key before inspecting the value
            print(f"{indent_str}  - Key: '{key}'")
            inspect_structure(value, indent=indent + 2)

#inspect_structure(predictions)

# src/utils.py

def format_text(text: str) -> str:
    """Format the input text by stripping leading/trailing whitespace and capitalizing."""
    return text.strip().capitalize()

def validate_data(data: dict) -> bool:
    """Validate the input data for the bot."""
    # Example validation: check if required keys exist
    required_keys = ['name', 'message']
    return all(key in data for key in required_keys)

def helper_function_example() -> str:
    """An example of a helper function for the bot."""
    return "This is a helper function result."
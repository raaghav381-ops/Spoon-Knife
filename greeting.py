def greet(name="World"):
    """Return a friendly greeting message.

    Args:
        name: Name to greet. Empty or blank defaults to 'World'.

    Example:
        >>> greet("GitHub")
        'Hello, GitHub! Welcome to our shared project.'
    """
    if not name or not str(name).strip():
        name = "World"
    return f"Hello, {str(name).strip()}! Thanks for collaborating on our shared project."

def add(a, b):
    """Simple add function - example feature addition."""
    return a + b

if __name__ == "__main__":
    print(greet("GitHub"))
    print(greet(""))  # edge-case: empty string
    print(f"2 + 3 = {add(2, 3)}")

def greet(name="World"):
    """Return a friendly greeting message."""
    return f"Hello, {name}! Welcome to fork-and-PR practice."

def add(a, b):
    """Simple add function - example bug-fix / feature addition."""
    return a + b

if __name__ == "__main__":
    print(greet("GitHub"))
    print(f"2 + 3 = {add(2, 3)}")

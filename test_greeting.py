from greeting import greet, add

def test_greet_normal():
    assert greet("GitHub") == "Hello, GitHub! Welcome to fork-and-PR practice."

def test_greet_empty():
    assert greet("") == "Hello, World! Welcome to fork-and-PR practice."
    assert greet("   ") == "Hello, World! Welcome to fork-and-PR practice."

def test_add():
    assert add(2, 3) == 5

if __name__ == "__main__":
    test_greet_normal(); test_greet_empty(); test_add()
    print("All tests passed!")

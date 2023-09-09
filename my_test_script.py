import time

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def test_addition():
    """Test the addition function."""
    result = add(2, 3)
    assert result == 5, f"Expected 5 but got {result}"
    time.sleep(10)

if __name__ == "__main__":
    test_addition()
    print("Test passed successfully.")

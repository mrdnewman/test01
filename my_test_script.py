import time
import os

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def test_addition():
    """Test the addition function."""
    result = add(2, 3)
    assert result == 5, f"Expected 5 but got {result}"

countdown = 0
while countdown > 0:
    # Display the countdown number
    print(countdown)
    
    # Pause for 1 second
    time.sleep(1)
    
    # Clear the screen (works on Unix-like systems, might not work on all platforms)
    os.system('clear')  # For Windows, you can use 'cls' instead of 'clear'
    
    # Decrement the countdown
    countdown -= 1

# Clear the screen one last time
os.system('clear')

if __name__ == "__main__":
    test_addition()
    print("Test passed successfully.")

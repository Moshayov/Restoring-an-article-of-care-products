import random

# Generate 40 random numbers between 1 and 10,000
random_numbers = [random.randint(1, 1900) for _ in range(10)]

# Sort the numbers in ascending order
random_numbers.sort()

# Print the sorted numbers
print(random_numbers)

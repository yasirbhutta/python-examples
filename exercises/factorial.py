# Python exercises for Beginners
# youtube@YasirBhutta

# Get user input
number = int(input("Enter non-negative number:"))

if number < 0:
    print("Factorial is not defined for negative numbers.")
    result = None
elif number == 0 or number ==1:
    result = 1
else:
    result = 1
    for i in range(2, number + 1):
        result *= i

if result is not None:
    print("Factorial of", number, "is", result)

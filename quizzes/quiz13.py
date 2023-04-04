# Define a function called add with two required arguments, a and b, and an optional tuple of additional arguments called parn.
def add(a, b, *parn):
    # Initialize a variable called total to 0.
    total = 0
    
    # Print the sum of a and b to the console.
    print(a + b)
    
    # Use a for loop to iterate through the values in parn and add them to the total variable.
    for n in parn:
        total += n
    
    # Return the value of total.
    return total

# Call the add function with the arguments 1 and 2.
print(add(1, 2))


# You can also follow me on:

# Website: https://yasirbhutta.github.io/
# Facebook: https://www.facebook.com/yasirbhutta786/
# YouTube:https://youtube.com/@YasirBhutta
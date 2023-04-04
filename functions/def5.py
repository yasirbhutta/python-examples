# Define a function called "add" that takes any number of arguments using the special syntax "*args".
def add(*args):
    # Initialize a variable called "total" to 0.
    total = 0
    # Iterate over each argument in "args".
    for n in args:
        # Add the current argument to the "total" variable.
        total += n
    # Return the final value of "total".
    return total

# Call the "add" function with three arguments: 1, 2, and 3.
# The output should be 6, since the sum of 1, 2, and 3 is 6.
print(add(1, 2, 3))

# Call the "add" function with two arguments: 4 and 5.
# The output should be 9, since the sum of 4 and 5 is 9.
print(add(4, 5))

# Call the "add" function with one argument: 8.
# The output should be 8, since the sum of 8 is 8.
print(add(8))

# Call the "add" function with no arguments.
# The output should be 0, since there are no arguments to add.
print(add())



# You can also follow me on:

# Website: https://yasirbhutta.github.io/
# Facebook: https://www.facebook.com/yasirbhutta786/
# YouTube:https://youtube.com/@YasirBhutta
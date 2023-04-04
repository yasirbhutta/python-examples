# Define a function called "greet" that takes any number of keyword arguments using the special syntax "**kwargs".
def greet(**kwargs):
    # Iterate over each keyword argument in "kwargs".
    for key, value in kwargs.items():
        # Print the current keyword argument to the console.
        print(f"{key}: {value}")

# Call the "greet" function with three keyword arguments: "name", "age", and "hobby".
# The output should be:
# name: Hamza
# age: 25
# hobby: reading
greet(name="Hamza", age=25, hobby="reading")

# Call the "greet" function with two keyword arguments: "city" and "country".
# The output should be:
# city: Multan
# country: Pakistan
greet(city="Multan", country="Pakistan")

# Call the "greet" function with no keyword arguments.
# The function will execute, but it will print nothing to the console.
greet()

# You can also follow me on:

# Website: https://yasirbhutta.github.io/
# Facebook: https://www.facebook.com/yasirbhutta786/
# YouTube:https://youtube.com/@YasirBhutta

import random
i = random.randint(0,9)
print(f"{i = }")
j = random.randint(0,9)
print(f"{j = }")
i = i + j
j = i - j
i = i - j
print("==========")
print("new i value =", i)
print("new j value=", j)

# This program imports the 'random' module to generate random integers.
# Two random integers between 0 and 9 are generated and assigned to variables 'i' and 'j', respectively.
# The values of 'i' and 'j' are output to the console using formatted string literals.
# The values of 'i' and 'j' are swapped without using a third variable.
# The new values of 'i' and 'j' are output to the console.

# Website: https://yasirbhutta.github.io/
# Facebook: https://www.facebook.com/yasirbhutta786/
# YouTube:https://youtube.com/@YasirBhutta
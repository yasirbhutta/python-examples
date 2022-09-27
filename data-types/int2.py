# https://yasirbhutta.blogspot.com/
# Python - Convert String to int
str1 = "2008"  # string
str2 = '14'    # string
# int() function 
# Return an integer object from string
print(int(str1)+int(str2))


# How to Convert a Python integer to string
num1 = 36
num2 = 14
sum = num1+ num2

# the '+' does not automatically convert 
# numbers or other types to string form.
## print("Total = " + sum ) ## NO, does not work

print("Total = " + str(sum)) ## yes

# Convert to octal and hexadecimal

print (oct(64), hex(64), hex(255))

print(int())

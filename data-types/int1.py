# https://yasirbhutta.blogspot.com/2022/09/python-numeric-types-int.html
# int data type variables
# assigning integer, hexadecimal and octal literal to int type variable in Python
 
#int literal
var1 = 1
var2 = 10
print(var1)
print(var2)

#To indicate a hexadecimal literal, use 0x
num = 0xA0F #Hexa-decimal
print("Hexa-decimal=" + str(num))

#To denote an octal literal, use 0 (or 0o)
num = 0o37 #Octal
# the '+' does not automatically convert numbers or other types to string form. 
# Python str() function returns the string version of the object.
print("Octal = " + str(num))
# The type() function is used to get the type of an object.
print(type(num)) 
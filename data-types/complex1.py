# https://yasirbhutta.blogspot.com/
# Python data types - complex

z = 3 + 2j
print(z)       ## Output -  (3+2j)                
print(type(z)) ## Output - <class 'complex'>

##
# use of floating-point numbers to create complex number
z = 3.14 + 2.71j
## isinstance() function 
##  to check if an object belongs to a particular class.
print(isinstance(1+2j,complex)) ## Output - True

print(2 + 3j + 4 + 5j) ## Output - (6+8j)

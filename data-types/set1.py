# https://yasirbhutta.github.io/python/
# https://web.facebook.com/groups/pythontips

#  Python Set Types - set
set1 = {3,5,6,1,0,7}
print(set1)       #Output:  {0, 1, 3, 5, 6, 7}
print(type(set1)) #Output:  <class 'set'>

# add element in set
set1.add(2)
print(set1)       #Output:  {0, 1, 2, 3, 5, 6, 7}

# remove elements from a set
set1.remove(6)
print(set1)       #Output:  {0, 1, 2, 3, 5, 7}

# update set
set2 = {12,8,19}
set1.update(set2)
print(set1)       #Output:  {0, 1, 2, 3, 5, 7, 8, 12, 19}
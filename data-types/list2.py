# https://yasirbhutta.blogspot.com/
# https://web.facebook.com/groups/pythontips

## Python List Slicing
thislist=["red","green","blue","yellow",
 "pink", "black"]
## lst[start:end] 
print(thislist[2:5]) ##Output: ['blue', 'yellow', 'pink']
##end

## List items can be of any data type
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

### list with mixed data types
list1 = ["abc", 34, True, 40, "male"]

print(list1) ##Output: ['abc', 34, True, 40, 'male']


# Python Nested List
n_list = ["Python", [2, 0, 1, 5]]

# Nested indexing
print(n_list[0][1]) ##Output:  y

print(n_list[1])    ##Output:  [2, 0, 1, 5]
print(n_list[1][2]) ##Output:  1   



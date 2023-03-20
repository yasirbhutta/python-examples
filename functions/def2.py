# This function finds the maximum value in a list of numbers
def find_max(numbers):
  max_value = numbers[0] # set the initial max value to the first element in the list
  for num in numbers: # iterate over each element in the list
    if num > max_value: # if the current element is greater than the current max value
         max_value = num # set the max value to the current element
  return max_value # return the final max value

# Example usage
my_list = [4,2,8,10,1,5,9]
print(find_max(my_list)) # prints 10


# You can also follow me on:

# Website: https://yasirbhutta.github.io/
# Facebook: https://www.facebook.com/yasirbhutta786/
# YouTube:https://youtube.com/@YasirBhutta
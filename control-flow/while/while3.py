# Youtube@YasirBhutta
# Sum of given numbers till the number entered is zero
sum = 0
number = int(input("enter the number: "))

while number != 0:
    sum += number
    number = int(input("Enter another number:"))

print(f'The sum of the number is {sum}')


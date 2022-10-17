## https://yasirbhutta.github.io/python
## Python break statement

print('-- Help: type "quit" to exit --')
while True:
    num1 = input('Enter number to check is odd or even: ')
    if num1.lower() == 'quit':
        break
    elif int(num1)%2 == 0:
        print ('Number is even: ', num1)
    else:
        print('Number is odd: ',num1)
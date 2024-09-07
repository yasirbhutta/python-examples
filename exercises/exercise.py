# Python Exercises for Beginners
# youtube@YasirBhutta
num = 5
result = None
if num < 0:
    print("Factorial is not defined")
elif num==0 or num ==1:
    result=1
else:
    result = 1
    for i in range(1, num + 1):
        print(f"before exec i = {i}, result = {result}")
        result *= i
        print(f"after exec result = {result}")
if result is not None:
    print(f"Factorial of {num} is {result}")


def foo(x):
    if x == 1:
        return 1
    else:
      return x * foo(x - 1)
print(foo(5))
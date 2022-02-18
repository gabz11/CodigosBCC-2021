def f(x):
    y = x ** 2
    x = x + 1
    return y


def g(x):
    x = x + 1
    y = x ** x
    return y


x = 5
y = f(x)
print(x)
print(y)
y = g(x)
print(x)
print(y)

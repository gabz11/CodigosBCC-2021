def f(x):
    return x + 1
def g(x):
    return x - 1


x = 1
resultado = f(g(f(g(x))))
print(x)
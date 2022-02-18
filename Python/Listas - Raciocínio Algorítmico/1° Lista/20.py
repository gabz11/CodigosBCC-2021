def f(x):
    y = x % 10
    return y
def g(x):
    y = x*10
    return y


x = 11
z = g(f(x))
print(y, z)
# Não executaria
def rendering(x):
    for i in range(1, x+1, 2):
        yield i
odd = rendering(15)
print(next(odd))
print(next(odd))
print(next(odd))
print(next(odd))
print(next(odd))
print(next(odd))
print(next(odd))
print(next(odd))
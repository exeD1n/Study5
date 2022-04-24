src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []

b = 1
while b != len(src):
    if src[b] > src[b - 1]:
        result.append(src[b])
    b += 1

print(result)
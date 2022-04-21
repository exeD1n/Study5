import sys

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
j = []

def lobash():
    for i in src:
        if src.count(i) == 1:
            j.append(i)
    print(j)
    print(sys.getsizeof(j))

def interengent():
    j = (i for i in src if src.count(i) == 1)
    print(list(j))
    print(sys.getsizeof(j))
    
    
if __name__ == "__main__":
    lobash()
    interengent()
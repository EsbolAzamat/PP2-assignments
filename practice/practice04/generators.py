# Task 1
def gen(N):
    i = 1
    while N >= i * i:
        yield i * i
        i +=1

N = int(input())
print(*gen(N))

# Task 2

def even(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input())
print(*even(n), sep=",")

# Task 3

def dev(x):
    for i in range(x + 1):
        if i % 12 == 0:
            yield i

x = int(input())
print(*dev(x))

# Task 4
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

a, b = map(int, input().split())
for i in squares(a, b):
    print(i, end=" ")

# Task 5 

def down(m):
    while m >= 0:
        yield m
        m -= 1
    
m = int(input())
print(*down(m))
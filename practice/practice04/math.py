import math

# Task 1
n = int(input())
print(math.radians(n))  

# Task 2

h, a, b = map(int, input().split())
print((a+b)/2 * h) 

# Task 3

sides, length = map(int, input().split())

print(int(pow(length, 2) * sides/ (4 * math.tan(math.radians(180 / sides)))))


# Task 4

l, H = map(int, input().split())  
print(l * H)
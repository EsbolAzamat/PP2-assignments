import re


with open('raw.txt', 'r', encoding='utf-8') as file:
    data = file.read()

# Task 1
res = re.search(r'ab*', data)
if res:
    print('Match')
else:
    print('No match')


# Task 2
res = re.search(r'ab{2,3}', data) 
if res:
    print('Match')
else:
    print('No match')


# Task 3
res = re.search(r'[a-z]+_[a-z]+', data) 
if res:
    print('Match')
else:
    print('No match')


# Task 4
res = re.search(r'[A-Z][a-z]+', data) 
if res:
    print('Match')
else:
    print('No match')



# Task 5
res = re.search(r'a.*b', data) 
if res:
    print('Match')
else:
    print('No match')


# Task 6
res = re.sub(r'[ ,.]+', r':', data)
print(res)


# Task 7
res = re.sub(r'_([a-z])', lambda x: x.group(1).upper(), data)
print(res)



# Task 8
res = re.split(r'?=[A-Z]', data)
print(res)

# Task 9
res = re.sub(r'([a-z])([A-Z])', r'\1 \2', data)
print(res)

# Task 10
res = re.sub(r'([a-z])([A-Z])', r'\1_\2', data)
print(res)

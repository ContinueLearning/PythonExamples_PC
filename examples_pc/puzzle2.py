##Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.

l=['a', 'e', 'i', 'o', 'u']
concat=""

for i in l:
    print(concat)
    concat=""
    for k in l:
        concat=concat+k
            
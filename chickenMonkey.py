'''
this is chickenMonkey but for Python
'''

for i in range(1, 101):
    if i % 5 == 0 and i % 7 == 0:
        print(i, "ChickenMonkey")
    elif i % 5 == 0:
        print(i, "Chicken")
    elif i % 7 == 0:
        print(i, "Monkey")

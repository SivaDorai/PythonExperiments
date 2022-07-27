a = [1, 2, 3, 4, 5]
b = int(input("enter a number"))
for i in a:
    if i == b:
        print(a.index(i))
if i != b:
    print("number doesn't exist")


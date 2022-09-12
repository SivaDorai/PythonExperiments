import itertools
mylist=[3,1,6,7,2]
counter=0
res=[]
maxelem = max(mylist)
for index, value in enumerate(mylist):
    if value == maxelem:
        counter= len(mylist)

    elif value == min(mylist):
        counter = 1
    else:
        counter=0
    res.append(counter)
print(res)
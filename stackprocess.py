def getSum(A: int,B: int,C: int):
    s=(A,B,C)
    for i in s:
        print(i)
        if i >=1 and i <=100:
            return A+B+C
#print(getSum(5,0,7))

from typing import List
def getMaxAdditionalDiners(N: int, K: int, M: int, S: List[int])-> int:
    additionalDiners=0
    for i in range (1,N+1):
        compare_set = [i,i+K,i-K]
        check = any(item in compare_set for item in S)
        if check == False:
            additionalDiners+=1
            S.append(i)
    print(additionalDiners,S)

#getMaxAdditionalDiners(15,2,3,[11,6,14])


"""
A circular dial consists of digits around its boundary ranging to N. 
K digit secret code is set using the dial. 
Dial can be moved 1 position left or right at a time. Each move takes a second.
Find the time taken to dial to a given code. Start position will be 1.

Sample data - 10 digits, Code 9738
From 1 to 9 - Reverse pass - 1-10-9 - 2 moves Forward pass - 1-2-3-..-9 
Since forward is long better option is reverse. Likewise find the optimal time.
"""

def findtimetounlock(N: int, K: int, code:str)->int:
    currentpos  = 1
    secstomoveby1pos = 1
    dial = []
    for i in range(1,N+1):
        dial.append(i)
    timetaken  = 0
    for j in code:
        gotopos = dial.index(int(j))+1
        forward = abs(gotopos - currentpos)
        reverse = currentpos - gotopos + N
        if forward < reverse:
            timetaken = timetaken + forward
        else:
            timetaken = timetaken + reverse
        currentpos = gotopos
    print(timetaken)
    return 0

findtimetounlock(10,4,"9616")

"""
Find distance of K nearest points to the origin in 2D plane
[(-3,4),(0,5),(2,1),(1,-3)]
"""




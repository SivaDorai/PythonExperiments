#https://www.metacareers.com/profile/coding_puzzles/?puzzle=990060915068194
"""
A circular dial consists of digits around its boundary ranging to N.
K digit secret code is set using the dial.
Dial can be moved 1 position left or right at a time. Each move takes a second.
Find the time taken to dial to a given code. Start position will be 1.

Sample data - 10 digits, Code 9738
From 1 to 9 - Reverse pass - 1-10-9 - 2 moves Forward pass - 1-2-3-..-9
Since forward is long better option is reverse. Likewise find the optimal time.
"""
import queue
from typing import List
def findtimetounlock(N: int, K: int, C:List[int])->int:

    timetaken  = 0
    if C[0]!=1:
        C.insert(0,1)
    for j in range(C.__len__()-1):
        forward = abs(C[j+1]-C[j])
        reverse = N - forward
        timetaken = timetaken + min(forward, reverse)
    return timetaken

#print(findtimetounlock(10,4,[9,4,4,8]))

def getMinCodeEntryTime(N: int, M: int, C:List[int])->int:
    LCode=[1]
    RCode=[1]
    time = 0
    #C.insert(0, 1)
    if N < 3 or N > 1000000000 or M < 1 or M > 3000:
        return time
    for i in range(M):
        if C[i] != C[i - 1]:  # ignore if nos are consecutive
            lftime = abs(C[i] - LCode[- 1])
            lrtime = N-lftime
            lmin = min(lftime, lrtime)
            rftime = abs(C[i] - RCode[-1])
            rrtime = N - rftime
            rmin = min(rftime, rrtime)
            time += min(lmin, rmin)
            if lmin < rmin:
                LCode.append(C[i])
            else:
                RCode.append(C[i])

    print(LCode, RCode)
    return time

print(getMinCodeEntryTime(10,4,[9,4,4,8]))

def getMinCodeEntryTime2(N: int, M: int, C:List[int])->int:

    def findMin(N:int, curr:int, Lprev: int, Rprev: int):
        d = dict()
        lf = abs(Lprev-curr)
        lr = N-lf
        rf = abs(Rprev-curr)
        rr = N- rf
        if min(lf, lr)< min(rf, rr):
            d['lock'] = "l"
        else:
            d['lock'] = "r"
        d['time'] = min(lf, lr, rf, rr)

        return d

    LL= [1]
    LR = [1]
    time = 0
    lock = dict()
    for i in C:
        lock = findMin(N,i,LL[-1],LR[-1])
        time += lock.get('time')
        if lock.get("lock") == "l":
            LL.append(i)
        else:
            LR.append(i)
    return time

#print(getMinCodeEntryTime2(10,4,[9, 4,4,8]))

def getMinCodeEntryTime3(N: int, M: int, C:List[int])->int:

    time = 0
    C.insert(0, 1)

    if N < 3 or N > 1000000000 or M < 1 or M > 3000:
        return time
    for i in range(M):
        if i<1 or i>N:
            continue
        Lf = C[i] - C[i-1]
        Lr = N - Lf
        Rf = C[i] - C[i-1]
        Rr = N - Rf
        time += min(Lf, Lr, Rf, Rr)
        C.pop(i-1)

    return time

#print(getMinCodeEntryTime3(10,4,[9, 4,4,8]))
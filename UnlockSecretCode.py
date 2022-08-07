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

print(findtimetounlock(10,4,[9,4,4,8]))
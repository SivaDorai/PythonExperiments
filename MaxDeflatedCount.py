from typing import List
#https://www.metacareers.com/profile/coding_puzzles/?puzzle=183894130288005
def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
    # Write your code here
    deflate = 0
    if N>=1 and N<=50:
        for i in range(N-1, 0,-1):
            current = R[i]
            previous = R[i-1]
            if previous >= current:
                deflate += 1
                previous = previous - 1 - (previous-current)
                R[i - 1] = previous
                if previous<=0:
                    deflate=-1


    return deflate

print(getMinimumDeflatedDiscCount(4,[6,5,4,3]))
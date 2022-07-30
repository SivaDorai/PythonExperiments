from typing import List


# Write any import statements here
#https://www.metacareers.com/profile/coding_puzzles/?puzzle=348371419980095
def getMinProblemCount(N: int, S: List[int]) -> int:
    # Write your code here
    if N >= 1 and N <= 500000:
        if containsOdd(S):
            return int((max(S)/2)+1)
        else:
            return int(max(S)/2)


def containsOdd(S: List[int]) -> bool:
    for i in S:
        if i%2 != 0:
            odd = True
            break
        else:
            odd = False
    return odd

print(getMinProblemCount(4, [4,3,3,4]))
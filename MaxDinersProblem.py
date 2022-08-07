#https://www.metacareers.com/profile/coding_puzzles/?puzzle=203188678289677
from typing import List
def getMaxAdditionalDiners(N: int, K: int, M: int, S: List[int])-> int:
    additionalDiners=0
    start=1
    end= N
    seats = list(range(1,N+1))
    for i in seats:
        if i not in S:
            S.append((i))
            list(range(K))

        continue
    return additionalDiners

getMaxAdditionalDiners(15,2,3,[11,6,14])
#https://www.metacareers.com/profile/coding_puzzles/?puzzle=203188678289677
from typing import List
def getMaxAdditionalDiners(N: int, K: int, M: int, S: List[int])-> int:
    additional = set()
    total = set(range(1,N+1))
    for i in total:
        nxt = list(range(i + 1, i + K + 1))
        prev = list(range(i , i - (K + 1), -1))
        if i == 1:
            if set(nxt).intersection(S):
                continue
            else:
                S.append(i)
        elif i == N:
            if set(prev).intersection(S):
                continue
            else:
                S.append(i)
        else:
            if set(prev).intersection(S) or set(nxt).intersection(S):
                continue
            else:
                S.append(i)
        additional.add(i)
    return additional.__len__()

print(getMaxAdditionalDiners(15,2,3,[11,14,6]))

def getMaxAdditionalDiners2(N: int, K: int, M: int, S: List[int])-> int:
    # additionalDiners=N-((2*K)+M)
    # additionalDiners = additionalDiners/(2*K)
    # if N % 2!=0:
    #     additionalDiners =additionalDiners-1
    # return int(additionalDiners)
    print(range(1,3))
print(getMaxAdditionalDiners2(10,1,2,[2,6]))

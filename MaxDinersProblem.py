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
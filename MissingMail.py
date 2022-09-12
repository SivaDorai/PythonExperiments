from typing import List
from timeit import default_timer as timer
# Write any import statements here

def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
  # Write your code here

    if S == 0:
        return sum(V) - C
    if S == 1:
        return sum(list(map(lambda x: x-C if x > C else 0, V)))

    try:
        possibilities = list_possibilities(N,V[-1],C)
        print(possibilities)
        start_time = timer()
        W = V.copy()
        profit = 0
        result = []
        for a in possibilities:
            for k in range(N):
                if V[k] < C and a[k] == '1':
                    continue
                if a[k] == '0':
                    if k + 1 < N:
                        V[k + 1] += V[k] * (1 - S)
                        V[k]=0
                else:
                    profit += V[k] - C
            result.append(profit)
            profit = 0
            V = W.copy()
        end_time = timer()
        print("Process time", end_time - start_time)
        print(result)

        return max(result)
    except Exception as e:
        print(e.with_traceback())


def list_possibilities(N:int, lastdaypackage: int, delivery_cost:int) -> list:
    X = pow(2, N - 1)-1
    possibilities =[]
    for i in range(X):
        y = (str(bin(i))[2:]).zfill(N-1)
        possibilities.append(y + "1")
        if lastdaypackage < delivery_cost:
            possibilities.append(y + "0")

    return possibilities



print(getMaxExpectedProfit(5, [10,2,8,6,4],3,0.15))
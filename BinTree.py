from typing import List


# Write any import statements here

def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
    # Write your code here
    if S == 0:
        return sum(V) - C
    if S == 1:
        return sum(list(map(lambda x: x-C if x > C else 0, V)))
    try:
        X = pow(2, N - 1) - 1
        possibilities = []
        for i in range(X):
            y = (str(bin(i))[2:]).zfill(N - 1)
            possibilities.append(y + "1")
            if V[-1] < C:
                possibilities.append(y + "0")

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
                else:
                    profit += V[k] - C
            result.append(profit)
            profit = 0
            V = W.copy()

        print(possibilities)
        print(result)
        return max(result)
    except RuntimeError as re:
        print(re)

print(getMaxExpectedProfit(5, [10,2,8,6,4],3,.5))
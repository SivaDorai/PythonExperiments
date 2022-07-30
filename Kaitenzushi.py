#https://www.metacareers.com/profile/coding_puzzles/?puzzle=958513514962507
from typing import List
# Write any import statements here

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  # Write your code here
    want=[]
    maxDishCount = 0
    if N >=1 and N<500000 and K<=N and K>=1 :
      for i in D:
          if i >= 1 and i <= 1000000:
              if i not in want[-K::]:
                  want.append(i)
                  maxDishCount+=1
      print(maxDishCount)
    return maxDishCount

getMaximumEatenDishCount(6,[1,2,3,3,2,1],1)

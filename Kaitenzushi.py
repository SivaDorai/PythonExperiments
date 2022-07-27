#https://www.metacareers.com/profile/coding_puzzles/?puzzle=958513514962507
from typing import List
# Write any import statements here

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  # Write your code here
    want=[]
    maxDishCount = 0
    if N >=1 and N<500000 and K<=N and K>=1 :
      for i in D:
          if i not in want[-K::]:
              want.append(i)
              maxDishCount+=1
      print(want)
    return maxDishCount


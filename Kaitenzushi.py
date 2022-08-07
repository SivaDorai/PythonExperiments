#https://www.metacareers.com/profile/coding_puzzles/?puzzle=958513514962507
from typing import List
# Write any import statements here

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  # Write your code here
    want=[]
    for i in D:
      if i not in want[-K::]:
          want.append(i)


    return want.__len__()

getMaximumEatenDishCount(6,[1,2,3,3,2,1],1)

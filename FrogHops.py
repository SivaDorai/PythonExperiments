#https://www.metacareers.com/profile/coding_puzzles/?puzzle=977526253003069
from typing import List
# Write any import statements here

def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
  # Write your code here
  #N-lilypads, F- Frogs
  # sort P - pods occupied by frogs
  P.sort()
  podpositions = []
  hops=0
  for i in range(1,N+1):
      if i not in P:
          podpositions.insert(i,0)
      else:
          podpositions.insert(i,1)
  for j in range(N):
      if podpositions[j] ==0:
          pass
      else:
          for k in range(j+1,N+1):
              if podpositions[k]==0:
                  hops+=1
                  podpositions[j]=0
                  podpositions[k]=1
                  if k==N-1 and podpositions[k]==1:
                      podpositions[k] = 0
                  break
      print(podpositions)

  return hops

print(getSecondsRequired(3,1,[1]))
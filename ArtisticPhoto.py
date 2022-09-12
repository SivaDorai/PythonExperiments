# Write any import statements here
import re

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Write your code here
  #PAB and #BAP are valid patterns. Pattern can have only one P, A and B. A should be between P and B.
  # Distance between P and A and A and B should be within X and Y
  if N < 1 or N > 200 or X < 1 or Y < 1:
    return 0
  l = list(C)
  BAP, PAB, possibilities= 0,0,0

  Aindexes = [index for index, element in enumerate(l) if element == "A"]

  for indexA in Aindexes:
    if not (indexA==0 or indexA== len(l)-1): # not considering A as valid if it comes at the ends
      # processing left side
      for i in range(indexA):
        if l[i] == ".":
          continue
        if l[i] =="B":
          if abs(i-indexA) in list(range(X,Y+1)) :
            for j in range(indexA + 1, len(l)):
              if l[j] =="P" and abs(j - indexA) in list(range(X, Y + 1)):
                BAP +=  1
        if l[i] == "P":
          if abs(i - indexA) in list(range(X,Y+1)) :
            for j in range(indexA + 1, len(l)):
              if l[j] =="B" and abs(j - indexA) in list(range(X, Y + 1)):
                PAB += 1



  return BAP+PAB


print(getArtisticPhotographCount(8,".PBAAP.B",1,3))
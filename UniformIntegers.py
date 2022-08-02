# Write any import statements here
#https://www.metacareers.com/profile/coding_puzzles/?puzzle=228269118726856
import math

def getUniformIntegerCountInInterval(A: int, B: int) -> int:
  # Write your code here
  if A >= 1 and B >= 1 and A <= pow(10, 12) and B <= pow(10, 12):
    lenofstartint = math.floor(math.log10(A) + 1)
    lenofendint = math.floor(math.log10(B) + 1)
    firstcharofmultiplier = 1
    temp = ''
    multiplier=[]
    if lenofendint < lenofstartint:
      return -1
    if lenofendint >= lenofstartint:
      for j in range(lenofstartint, lenofendint+1):
        for i in range(j):
          temp = str(temp) + str(firstcharofmultiplier)
        multiplier.append(temp)
        temp=''
    uniformint=0

    for k in multiplier:
      for j in range(1,10):
        current = j*int(k)
        if current>=A and current <= B:
          uniformint+=1
        if current>B:
          break
    return uniformint

print(getUniformIntegerCountInInterval(1,9))
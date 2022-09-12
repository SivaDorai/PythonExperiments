from typing import List
"""
Program to find a pair of nos from the list which equals the sum
"""

def sumofapair(nos: List[int], sum:int) -> List[int]:
    compliment= []
    for i in nos:
        j = sum -i
        if j>0:
            if j in compliment:
                print(j,i)
                return [j,i]
            else:
                compliment.append(i)

    return [0,0]

#sumofapair([8,2,6,4,9],11)



def twoSum(nums: List[int], target: int) -> List[int]:
    answer=[]
    for i in range(len(nums)):
        compliment = abs(target - nums[i])
        if compliment not in list(range(i+1, len(nums))):
            continue
        else:
            answer.append(i)
    return answer
print(twoSum([3,2,4,6],6))
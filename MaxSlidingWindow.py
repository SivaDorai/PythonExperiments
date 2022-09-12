"""
Sliding window of length k moves from left to right by 1 position - return max of the sliding window
"""
def maxslindingwindow(k:int,c:list[int])->list[int]:
    ret_arr=[]
    for i,v in enumerate(c):
        sub_arr= c[i:i+k]
        #if len(sub_arr)==k:
        ret_arr.append(max(c[i:i+k]))
    for j in range(k-1):
        ret_arr.pop()
    return ret_arr

print(maxslindingwindow(3,[1,2,3,0,-1,2,5,1,7]))

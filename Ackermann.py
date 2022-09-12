"""
A(M,N)= N+1 IF M=0
= A(M-1,1) IF M>0 AND N=0
= A(M-1, A(M,N-1)) IF M>0 AND N>0

"""

def ackermann(m:int,n:int)->int:
    if m==0:
        return n+1
    if n==0 and m>0:
        ackermann(m-1,1)
    else:
        ackermann(m-1,ackermann(m,n-1))

print(ackermann(3,4))
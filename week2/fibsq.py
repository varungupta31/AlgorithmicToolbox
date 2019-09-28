def fibsq(n):
    curr=0
    next=1
    res=0
    for i in range(n+1):
        res+=curr**2
        curr,next=next,curr+next
    return res

n=int(input())
print(fibsq(n))

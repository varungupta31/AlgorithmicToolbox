#uses python3
def pisano_len(m):
    prev=0
    next=1
    for i in range(m*m+1):
        prev,next=next,(prev+next)%m
        if(prev==0 and next==1):
            return i+1
def get_fibo(n):
    if(n<=1):
        return n
    prev=0
    curr=1
    for i in range(n-1):
        (prev,curr)=(curr,prev+curr)
    return curr

def huge_fibo(n,m):
    rem=int(n%pisano_len(m))
    return get_fibo(rem) % m

if __name__=='__main__':


    n,m=map(int,input().split())
    print(huge_fibo(n,m))

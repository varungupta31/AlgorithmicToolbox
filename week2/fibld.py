#uses python3
def pisano_len(m):
    curr=0
    next=1
    for i in range(m*m+1):
        curr,next=next,(curr+next)%m
        if(curr==0 and next==1):
            return i+1

def get_fibo(n):
    if n<=1:
        return n
    else:
        curr=0
        next=1
        for i in range(n):
            curr,next=next,curr+next
        return curr
def get_last_sum(n):
    rem=int(n%pisano_len(10))

    return get_fibo(rem)

if __name__=='__main__':

	n=int(input())
	print((get_last_sum(n+2)-1)%10) #trick

#uses python3
def fibo_sum(m,n):
    curr=0
    next=1
    res=0
    for i in range(n+1):

        if(i>=m):
            res+=curr
        curr,next=next,next+curr
    return res
if __name__=='__main__':
	m,n=map(int,input().split())
	print(fibo_sum(m,n)%10)

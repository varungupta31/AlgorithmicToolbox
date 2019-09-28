#uses python3

def get_fibo(n):
    curr=0
    next=1
    for i in range(n):
        curr,next=next,curr+next
    return curr

if __name__=='__main__':
	n=int(input())
	print(get_fibo(n))

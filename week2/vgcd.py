#uses python3

def egcd(a,b):
    if(b>a):
        (a,b)=(b,a)
    if(b==0):
        return a
    else:
        return egcd(b,a%b)
if __name__=='__main__':
	(a,b)=map(int,input().split())
	print((egcd(a,b)))

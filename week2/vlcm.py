#uses python3
def vlcm(a,b):
    def gcd(x,y):
        if(x<y):
            (x,y)=(y,x)
        if(y==0):
            return x
        else:
            return gcd(y,x%y)
    return (a*b)//gcd(a,b)

if __name__=='__main__':

    a,b=map(int,input().split())
    print((vlcm(a,b)))

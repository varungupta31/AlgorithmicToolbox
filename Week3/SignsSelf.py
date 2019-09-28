from operator import itemgetter

def MinVisits(n,cordinates):
    cordinates.sort(key=itemgetter(1))
    index=0
    res=[]
    while(index<n):
        curr=cordinates[index]
        while(index<n-1 and curr[1]>=cordinates[index+1][0]):
            index+=1
        res.append(curr[1])
        index+=1
    print(len(res))
    for val in res:
        print(val,end=" ")
if __name__=='__main__':
    cordinates=[]
    n=int(input())
    for _ in range(n):
        (x,y)=map(int,input().split())
        cordinates.append([x,y])
    MinVisits(n,cordinates)

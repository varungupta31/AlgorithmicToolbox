def distribute_candy(n):
    count=0
    i=1
    lst=[]
    candiesRem=n
    while(candiesRem>0):

        candiesRem-=i

        if(candiesRem>=i+1):
            lst.append(i)
            i+=1
            continue
        else:
            lst.append(n-sum(lst))
            return lst
    return lst

if __name__=='__main__':
    n=int(input())
    res=distribute_candy(n)
    print(len(res))
    for val in res:
        print(val, end=" ")

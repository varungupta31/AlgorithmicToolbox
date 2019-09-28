#uses python3
class Looter:
     def __init__(self,wt,val,item):
         self.wt=wt
         self.val=val
         self.item=item
         self.cost=val//wt

     def __lt__(self,other):
         return (self.cost<other.cost)
class KnapSack:
    def getMaxLoot(wt,val,capacity,items):
        ival=[]
        for i in range(items):
            ival.append(Looter(wt[i],val[i],i))
        ival.sort(reverse = True)

        totalval=0
        for i in ival:
            currwt=int(i.wt)
            currval=int(i.val)
            if capacity-currwt>=0:
                capacity-=currwt
                totalval+=currval
            else:
                fraction= capacity/currwt
                totalval+=currval*fraction
                capacity=int(capacity-(currwt*fraction))
                break
        return '%0.5f'%(totalval)
if __name__=='__main__':
    items,capacity=map(int,input().split())
    val=[]
    wt=[]
    for i in range(items):
        x,y=map(int,input().split())
        val.append(x)
        wt.append(y)
    print(KnapSack.getMaxLoot(wt,val,capacity,items))

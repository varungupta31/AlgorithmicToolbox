# python3
import sys


def compute_min_refills(distance, tank, stops):
    numfil=0
    curfil=0
    n=len(stops)
    stops.insert(0,0)
    stops.append(distance)

    while(curfil<=n):
        lastfil=curfil
        while(curfil<=n and (stops[curfil+1]-stops[lastfil])<=tank):
            curfil+=1
        if(curfil==lastfil):
            return -1
        if(curfil<=n):
            numfil+=1
    return numfil



if __name__ == '__main__':
    d=int(input())
    m=int(input())
    num=int(input())
    stops=list(map(int,input().split()))
    print(compute_min_refills(d, m, stops))

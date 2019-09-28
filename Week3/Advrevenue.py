#uses python3
def maxRev(n,profit_click,clicks):
    profit_click.sort()
    clicks.sort()
    res=0
    for i in range(n):
        res+=int(profit_click[i]*clicks[i])
    return res
if __name__=='__main__':
    n=int(input())
    profit_click=list(map(int, input().split()))
    clicks=list(map(int, input().split()))
    print(maxRev(n,profit_click,clicks))

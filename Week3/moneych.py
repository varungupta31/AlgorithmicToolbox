#uses python3

def money_ch(amt):
    #1,5,10 coins
    count=0
    while(amt>0):
        if(amt>=10):
            mul=amt//10
            count+=mul
            amt=amt-(10*mul)

        elif(amt>=5):
            mul=amt//5
            count+=mul
            amt=amt-(5*mul)

        elif(amt<5):

            count+=amt
            amt=amt-(1*amt)

    return count

if __name__=='__main__':
    print(money_ch(int(input())))

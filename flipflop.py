def palindrome(w):
    e = len(w) - 1
    s = 0
    while(s<e):
        if(w[s] != w[e]):
            return False
        s+=1
        e-=1
    return True

w =(1,2,3,4,5,6)

if (palindrome(w)): 
    print("The tuple is flip flop")
else:
    print("The tuple is not flip flop")

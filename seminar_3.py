'''def F(n,cache):
    if n==0 or n==1:
        cache [n] =1
        return 1
    if cache [n]!=0:
        return cache [n]
    cache [n] = F(n-1,cache)+F(n-2,cache)
    return cache [n]

n=105
cache=[0 for i in range(n+1)]


print(F(n,cache))'''


'''
def F(x,n):
    if n ==1:
        return x
    if n%2==0:
        return F(x,n//2)**2
    else:
        return F(x,n-1)*x



def pow(x,n):
    res=1
    for i in range(n):
        res*=x
    return res'''




def triangle(h,depth=1,symbol='.'):
    if h%2!=0 and depth==h//2+1:
        print(symbol*depth)
        return
    if h%2==0 and depth==h//2:
        print(symbol*depth)
        print(symbol*depth)
        return


    print(symbol*depth)
    triangle(h,depth=depth+1)
    print(symbol*depth)

triangle(10)
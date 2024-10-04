#ex 1
n=int(input())
def fib(n):
    if n==1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(n))


#ex_2
n=int(input())
def f(n):
    d=2
    while d*d<=n:
        if n%d==0:
            print(d)
            n=n//d
        else:
            d+=1
    if n>1:
        print(n)
print(f(n))


#ex_3
def nod(a,b):
    while a != b:
        if a > b:
            a = a-b
        if a < b:
            b = b-a
    return a


mini = 19371937193719371937
ansx = 0
ansy = 0
a,b = map(int,input().split())
for x in range(-100,100):
    for y in range(-100,100):
        if a*x + b*y == nod(a,b):
                if abs(x)+abs(y) < mini:
                    ansx = x
                    ansy = y
                    mini = abs(x) + abs(y)
                if abs(x) + abs(y) == mini:
                    if abs(x) < mini:
                        ansx = x
                        ansy = y
                        mini = abs(x)


print(ansx, ansy)


#ex_4
size=int(input())
def triangle(size,depth=1,symbol='C'):
    if size % 2 != 0 and depth == size // 2 + 1:
        print(symbol*depth)
        return

    print(symbol*depth)
    triangle(size,depth=depth+1,)
    print(symbol*depth)


triangle(size)


#ex_6
import numpy as np
x=np.array([0,1,2,3,4,5])
y=np.array([2,3,4,5,6,7])
k=(np.mean(x*y)-np.mean(x)*np.mean(y)) / (np.mean(x**2)-np.mean(x)**2)
b=np.mean(y)-k*np.mean(x)
print(k,b)


#ex_5
n=int(input())
m=int(input())
M=[[0 for i in range(m)] for j in range(n)]
x,y=0,0
d_x,d_y=0,1
M[0][0]=1
count=2

while count<=m*n:
    if (0<=x+d_x<=n-1) and (0<=y+d_y<=m-1) and (M[x+d_x][y+d_y])==0:
        M[x+d_x][y+d_y]=count
        count+=1
        x+=d_x
        y+=d_y
    else:
        if d_y==1:
            d_y = 0
            d_x= 1
        elif d_x == 1:
            d_x = 0
            d_y = -1
        elif d_y == -1:
            d_y = 0
            d_x = -1
        elif d_x == -1:
            d_x=0
            d_y=1

for s in M:
    print(*s)


















'''print('x y z w f')
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                if (x or not(y)) and not(y==z) and not(w):
                    f=1
                    print(x,y,z,w,f)
                else:
                    f=0'''

'''for n in range(100):
    s=bin(n)[2:]
    if n%3==0:
        r=s+s[-3:]
    else:
        d=bin((n%3)*3)[2:]
        r=s+d
    z=int(r,2)
    if z<76:
        print(n)'''


'''s=0
with open('9.csv') as f:
    for i in f:
        a=list(map(int,i.split(';')))
        if (max(a) < sum(a) - max(a)) and (a[0]+a[1]==a[2]+a[3] or a[0]+a[2]==a[1]+a[3] or a[0]+a[3]==a[1]+a[2]):
            s+=1
print(s)'''



'''for n in range(3,10000):
    s='5'+'2'*n
    while '52' in s or '2222' in s or '1122' in s:
        if '52' in s:
            s=s.replace('52','11',1)
        if '2222' in s:
            s=s.replace('2222','5',1)
        if '1122' in s:
            s=s.replace('1122','25',1)
    sum=s.count('5')*5+s.count('2')*2+s.count('1')*1
    if sum ==64:
        print(n)'''




'''f = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 -2024
c=0
while f:
    if f%25==0:
        c+=1
    f//=25
print(c)'''


'''import sys
sys.setrecursionlimit(10**6)
def F(n):
    if n>=2025:
        return n
    else:
        return n+3+F(n+3)

print(F(23)-F(21))'''

'''p=[]
s=[int(x) for x in open('17.txt')]
for i in range(len(s)-1):
    if ((s[i]>99 and s[i]<1000) or (s[i+1]>99 and s[i+1]<1000)) and (s[i]+s[i+1])%125==0:
        p.append(s[i]+s[i+1])
        p.sort()
print(p)
print(len(p))'''



'''sum=0
s=open('24_16333.txt').readline()
s=s.replace('W','Q').replace('R','Q').replace('2','1').replace('4','1')
while 'QQ' in s:
    s=s.replace('QQ','Q Q')
while '11' in s:
    s=s.replace('11','1 1')

print(max(len(c) for c in s.split()))'''


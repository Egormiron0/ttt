'''print('x y z w f')
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                if not(x<=z) or (y==w) or y:
                    f=1
                else:
                    f=0
                    print(x,y,z,w,f)'''


'''d=bin(64)[2:]
if 64%2==0:
    r='10'+d
else:
    r='1'+d+'01'
f=int(r,2)
print(f)'''

'''s=0
with open('9_16320(2).txt') as f:
    for i in f:
        a=list(map(int,i.split(';')))
        if (max(a)<sum(a)-max(a)) and (a[0]+a[1]==a[2]+a[3] or a[0]+a[2]==a[1]+a[3] or a[0]+a[3]==a[1]+a[2]):
            s+=1
print(s)'''

'''s='8'*82
while '1111' in s or '8888' in s:
    if '1111'in s:
        s=s.replace('1111','8',1)
    if '8888' in s:
        s=s.replace('8888','11',1)
print(s)'''



'''f = 2*729**2014 + 2*243**2016 - 2*81**2018 + 2*27**2020 - 2*9**2022 - 2024
c=0
while f:
    if f%27>9:
        c+=1
    f//=27
print(c)'''

'''import sys
sys.setrecursionlimit(10**6)
def F(n):
    if n==1:
        return 1
    else:
        return n*F(n-1)
print((F(2024)-F(2023))/F(2022))'''



'''def F(x,y):
    if x>y:
        return 0
    if x==y:
        return 1
    else:
        return F(x+1,y)+F(x*2,y)
print(F(3,6)*F(6,12)*F(12,16))'''

'''s=open('24.txt').readline()
s=s.replace('E','A').replace('O','A').replace('U','A').replace('L','K').replace('M','K').replace('N','K')
while 'AA' in s:
    s=s.replace('AA','A A')
while 'KK' in s:
    s=s.replace('KK','K K')
print(max(len(c) for c in s.split()))'''

'''from fnmatch import fnmatch
for i in range(2024,10**10+1,2024):
    if fnmatch(str(i),'10*2024?'):
        print(i//2024)'''




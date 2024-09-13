'''print('x y w z f')                                        №2
for x in range(0,2):
    for y in range(0,2):
        for w in range(0,2):
            for z in range(0,2):
                if ((z<=x) == (w<=y) or (x and w)):
                    f = 1
                else:
                    f = 0
                    print(x,y,w,z,f)'''



'''s=0                                                        №9
with open('9_13865.csv') as f:
    for i in f:
        a=list(map(int,i.split(';')))
        if (len(a)==len(set(a)) and 2*(max(a)+min(a))>3*(sum(a)-max(a)-min(a))) or (len(a)!=len(set(a)) and 2*(max(a)+min(a))<=3*(sum(a)-max(a)-min(a))):
            s+=1

print(s)'''





'''for n in range(3,3000):                                   №12
    s = '5' + '2'*n
    while '52' in s or '2222' in s or '1122' in s:
        if '52' in s:
            s=s.replace('52','11')
        if '2222' in s:
            s=s.replace('2222','5')
        if '1122' in s:
            s=s.replace('1122','25')
    sum = s.count('5')*5 + s.count('2')*2 + s.count('1')*1
    if sum == 64:
        print(n)'''


'''def convert_to(number,base,upper=False):                  №5
    digits='0123456789qwertyuiopasdfghjklzxcvbnm'
    if base>len(digits):return None
    result = ''
    while number>0:
        result=digits[number % base]+result
        number//=base
    return result.upper() if upper else result


p=[]
for n in range(1,10000):
    a=convert_to(n,3)
    if sum(map(int,a))% 4 ==0:
        s='1'+a
        l=s[:-2]
    else:
        d=3*sum(map(int,a))%4
        s=convert_to(d,3)
        l=a+s
    h=int(l,3)
    p.append(h)
    p.sort()
print(p)'''





'''f = 2*729**2014 + 2*243**2016 - 2*81**2018 + 2*27**2020 - 2*9**2022 -  2024       №14
count=0
while f:
    if f%27>9:
        count+=1
    f//=27

print(count)'''

'''s='0123456789ABCDEFGHIJK'
for x in s:
    for y in s:
        f=int(f'943697{x}21',21) - int(f'2{y}9253',21)
        if f%20==0:
            print(int(x,21)-int(y,21),f/20)'''



'''for a in range(-1000,1000):                            №15 
    if all(((a<x) or (x**2-7*x+10)>0) and((a>=y) or (y**2+7*y+12>0)) for x in range(-1000,1000) for y in range(-1000,1000)):
        print(a)'''

'''f=[]                                                   №17 
s=[int(x) for x in open('17_16328.txt')]
for i in range(len(s)-1):
    if s[i]%114==0 or s[i+1]%114==0:
        d=s[i]+s[i+1]
        f.append(d)
        f.sort()
print(f)'''


'''def F(x,y):                                    №23 
    if x>y or x==13:
        return 0
    if x==y:
        return 1
    return F(x+2,y)+F(x*3,y)+F(x**2,y)
print(F(3,49))'''


'''p=[]
for k in range(69):
    a=1+3*k-2*(68-k)
    p.append(a)
print(len(set(p)))'''

'''def F(x,y):
    if x<y or x==20:
        return 0
    if x==y:
        return 1
    else:
        return F(x-2,y)+F(x-3,y)+F(x//5,y)

print(F(41,10)*F(10,5))'''

'''def F(x,y):
    if x<y:
        return 0
    if x==y:
        return 1
    return F(x-1,y)+F(x-3,y)+F(x//2,y)

print(F(39,19)*F(19,16)*F(16,7))'''



'''                                                       №24
s=open('24_16333.txt').readline()
s=s.replace('W','Q').replace('R','Q').replace('2','1').replace('4','1')
while 'QQ' in s:
    s=s.replace('QQ','Q Q')
while '11' in s:
    s=s.replace('11','1 1')

print(max(len(c) for c in s.split()))'''


'''from fnmatch import fnmatch               №25 
for i in range(8387,10**9+1,8387):
    if fnmatch(str(i),'*75?122*'):
        print(i,i//8387)'''


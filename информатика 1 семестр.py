'''
f=open('ret.txt' , 'w')
f.write('-90'' ''0' + '\n')
f=open('ret.txt','a')
f.write('*' )

f=open('ret.txt','r')
c=f.readlines()
a=list(map(int,c[0].split()))
if c[1] == '+' :
    x=a[0]+a[1]
    g=open('u.txt','w')
    g.write(str(x))
if c[1]=='-':
    x=a[0]-a[1]
    g=open('u.txt','w')
    g.write(str(x))
if c[1]=='*':
    x=a[0]*a[1]
    g=open('u.txt','w')
'''



#ex_2
a,b=map(str,input().split())
a=int(a)
l=[b[i:i+a] for i in range(0,len(b),a)]
k=str()
for i in range(0,len(b)//a):
    k+=l[i][::-1]
print(k)


#ex_3
q=str(input())
s=list(q)
for i in range(len(s)):
    if s[i]=='E':
        s[i]='3'
    elif s[i]=='J':
        s[i]='L'
    elif s[i]=='S':
        s[i]='2'
    elif s[i]=='Z':
        s[i]='5'
    elif s[i]=='3':
        s[i]='E'
    elif s[i]=='L':
        s[i]='J'
    elif s[i]=='2':
        s[i]='S'
    elif s[i]=='5':
        s[i]='Z'
if s==list(q)[::-1] and set(q)<={'A','H','I','M','O','T','U','V','W','X','Y','1','8','E','J','S','Z','3','L','2','5'}:
        if q==q[::-1]:
            print('зеркальный палиндром')
        else: print('зеркальная строка')
else:
    if q==q[::-1]:
        print('палиндром')
    else:
        print('ничего')


#ex_5
import pandas as pd
from matplotlib import pyplot as plt
l=pd.read_csv('BTC_data.csv')
l1=l['time']
time=[]
for i in range(1457):
    time.append(l1[i][:10])

l4=l['close']
price=list(l4)

plt.figure(figsize=(8,6), dpi=100)
plt.plot(time,price)
plt.ylabel("price,$")
plt.xlabel("time,YY-MM-DD")
plt.title('цена биткоина')

plt.show()

#ex_4
import pandas as pd
from matplotlib import pyplot as plt
fig=plt.figure(figsize=(16,9))
ax1=fig.add_subplot(611)
ax2=fig.add_subplot(612)
ax3=fig.add_subplot(613)
ax4=fig.add_subplot(621)
ax5=fig.add_subplot(622)
ax6=fig.add_subplot(623)

df=pd.read_csv('iris_data.csv')
l1=df['SepalLengthCm']
l2=df['SepalWidthCm']
l3=df['PetalLengthCm']
l4=df['PetalWidthCm']

ax1.plot(l1,l2)
ax2.plot(l1,l3)
ax3.plot(l1,l4)
ax4.plot(l2,l3)
ax5.plot(l2,l4)
ax6.plot(l3,l4)
plt.show()









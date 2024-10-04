'''import numpy as np
x=np.array([0,1,2,3,4,5])
y=np.array([2,3,4,5,6,7])
k=(np.mean(x*y)-np.mean(x)*np.mean(y)) / (np.mean(x**2)-np.mean(x)**2)
b=np.mean(y)-k*np.mean(x)
print(k,b)
import numpy as np

a=np.array([1,1,1])
b=np.array([1,1,1])
print(a@b)

print(np.array([[1,2,3],[4,56,8],[0,0,5]]))'''

'''from matplotlib import pyplot as plt
x=[0,1,2,3,4,5,6,7,8]
y=[0,2,4,6,8,10,12,14,16]
plt.plot(x,y,'b--',label='2x')


import numpy as np
x2=np.arange(0,4.5,0.05)
plt.plot(x2,x2**2,'r--',label='x^2')


plt.title('My first graph')

plt.xlabel('X')
plt.ylabel('Y')

plt.show()'''


'''from matplotlib import pyplot as plt
x=[i for i in range(50)]
y=[j for j in range(50)]
s=[i+j for i in x for j in y]
plt.hist(s,bins =20)
plt.show()'''

'''import numpy as np
from matplotlib import pyplot as plt
fig=plt.figure(figsize=(16,9))
ax1=fig.add_subplot(221)
ax2=fig.add_subplot(222)
ax3=fig.add_subplot(223)
ax4=fig.add_subplot(224)

values=np.random.normal(0,10,1000)
ax1.hist(values,50)
plt.show()'''

'''
from matplotlib import pyplot as plt
import pandas as pd
df=pd.read_csv('iris_data.csv')

plt.hist(list(df['SepalWidthCm']),bins=50)
plt.show()'''


'''
a=set()
a.add(5)
a.add(23)
a.add(5)

b=set()
b.add(3)
b.add(4)
print(a|b)'''

n=4
m=4
a=[[0 for i in range(m)] for j in range(n)]


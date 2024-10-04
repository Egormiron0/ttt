'''#расстояние Левенштейна

a='aas'
b='asdasd'
def levenstein(a,b):
    len_a=len(a)
    len_b=len(b)
    res=[[-1 for i in range(len_b+1)] for j in range(len_a+1)]
    k=0
    for i in range(len_b+1):
        res[0][i]=k
        k+=1
    k=0
    for i in range(len_a+1):
        res[i][0]=k
        k+=1


    for i in range(1,len_a+1):
        for j in range(1,len_b+1):
            if a[i-1] == b[j-i]:
                res[i][j] = min(res[i-1][j]+1,res[i][j-1]+1,res[i-1][j-1])
            else:
                res[i][j] = min(res[i - 1][j] + 1, res[i][j - 1] + 1, res[i - 1][j - 1]+1)



    for s in res:
        print(*s)
    return res[-1][-1]


print(levenstein(a,b))'''


# наибольшая возрастающая подпоследовательность 
def LIS_slow(A):
    F=[0]*len(A)
    for i in range(len(A)):
        for j in range(i):
            if A[j]<A[i] and F[j]>F[i]:
                F[i]=F[j]
        F[i]+=1
    print(F)

LIS_slow([1,3,10,8,7,9])





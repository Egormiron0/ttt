f = open("эксперимент_2022-12-23_13-08-43.txt").readlines()
for i in range(0,4000,10):
    s=0
    l=[]
    for j in range(10):
        s+=int(f[i+j])
    print(int(s)-10,34)




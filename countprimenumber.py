l1=[3,5,4,7,8,9,2]
c=0
for i in l1:
    f=0
    for j in range(2,i):
        if(i%j==0):
            f=1
            break
        if(f==0):
            c+=1
            print("prime no: =",i)
            print("Total=",c)
# Q1
li=[1,2,3,4,8,7,9]
i=0
j=len(li)-1

while(i<j):
    temp=li[i]
    li[i]=li[j]
    li[j]=temp

    i=i+1
    j=j-1

print(li)    


# Q2
num=int(input("enter a number:"))
i=1
c=0
for i in range(1,num+1):
         if(num%i==0):
                c=c+1

if(c==2):
        print("prime")
else:
        print("not prime")       

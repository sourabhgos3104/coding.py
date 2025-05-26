 

num1=0
num2=1
a=int(input("enter your number:"))
i



li=[1,5,4,6,8,9,5,6,4,3]

for i in range(len(li)):
        for j in range(i+1,len(li)):
                if li[j]>li[i]:
                        temp=li[i]
                        li[i]=li[j]
                        li[j]=temp
print(li[1])
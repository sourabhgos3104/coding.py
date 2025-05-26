
li=[1,5,4,6,8,9,5,4,3]
for i in range(len(li)):
        for j in range(i+1,len(li)):
              if li[j]>li[i]:
                        temp=li[i]
                        li[i]=li[j]
                        li[j]=temp          
print(li[6]) 



li=[10,11,13,14,16,18,20]

for i in range(1,len(li)):
    if li[i]-li[i-1]>1:
               print(li[i]-1)

li=[41,21,52,25,34,56,88,55,57]

for i  in range(len(li)):
      for j in range(len(li)):
            if li[j]>li[i]:
                   
                   temp=li[i]
                   li[i]=li[j]
                   li[j]=temp

print(li) 



li=[41,21,52,25,34,56,88,55,57]

for i  in range(len(li)):
      for j in range(len(li)):
            if li[j]<li[i]:
                   
                   temp=li[i]
                   li[i]=li[j]
                   li[j]=temp

print(li)
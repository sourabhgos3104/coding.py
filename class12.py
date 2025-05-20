num=int(input("enter  a number:"))

ans=0
while(num>0):
    digit=num%10
    if(digit>ans):
        ans=digit
        num//=10

        print(ans)  



        

num=int(input("enter  a number:"))

ans=9
while(num>0):
    digit=num%10
    if(digit<ans):
        ans=digit
        num//=10
print(ans)    




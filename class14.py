# Q1
num=int(input("enter your number:"))
a=num
rev=0
while(num>0):
    digit=num%10
    rev=rev*10+digit
    num//=10
if(a==rev):
    print("pallidrom")
else:
    print("not")

# Q2
num=(input("enter your number:"))
a=num
print("pallidrom") if (a==num[::-1] ) else print("not pallidrom")

# Q3
num=int(input("enter a number:"))
a=0
b=num
while(num>0):
    digit=num%10
    a=digit*digit*digit+a
    num//=10

if(b==a):
    print("armstrong")    
else:
    print("not")


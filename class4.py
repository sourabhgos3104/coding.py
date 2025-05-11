
a=int(input("enter the number:"))
b=int(input("enter the number:"))
print(a) if(a>b) else print(b)



a=int(input("enter the number:"))
print("even") if(a%2==0) else print("odd")


a=int(input("enter the number:"))
print("multiple") if(a%5==0) else print("not an multiple")

age=int(input("enter the age:"))
print("eligible") if(age>18) else print("not eligible")

password=int(input("enter the password:"))
print("correct") if(password==12345) else print("not correct")



a=int(input("enter the number:"))
print("between") if(a>1 and a<100) else print("not in between")

s="hello"
print(s[0:1])
print(s[::])
print(s[::-1])


s="hello"
print(s[::-1])
print(s[::])
print(s[0:4])
print(s[0::2])
print(s[-1:1])
print(s[-1:-5:-1])
print(s[-1:-5:])
print(s[0:6])

print(s[::][0:1])


a=input("enter a number:")
print (a)

a=eval(input("enter a number:"))
print (a)


a=20
b=30
if a>b:
    print(a)
else:
    print(b)
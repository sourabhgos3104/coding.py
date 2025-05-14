pin=int(input("enter the password:"))
print("correct") if(pin==1234) else print("invalid")


b=input("enter the character:")
li=['a','e','i','o','u']

if (b  in li):
    print("vowel")
else:
    print("constant")



b=input("enter the value:")
print("vowel") if(b=='a'or b=='i' or b=='o'or b=='e' or b=='u') else print("constant")


age=int(input("enter your age:"))
print("eligible") if(age>18) else print("not eligible")


num=int(input("enter your number:"))
print("multiple") if(num%5==0) else print("not multiple")

print("welcome to restaurant")
print("menu:")
menu=[
     "1 burger : 50",
     "2 pizza : 40",
     "3 salad :50",
     "4 pasta : 70",
     "5 soda :50",

]
print(menu)

order=int(input("enter your option:"))

if(order==1):
    print("1 burger :50")

elif(order==2):
      print("2 pizza : 40")
      
elif(order==3):
      print("3 salad :50")

elif(order==4):
      print("4 pasta : 70")

      
elif(order==5):
      print("5 soda :50")

else:
      print("invalid")





print("student grade")
num=int(input("enter your number:"))

if(num>=0 and num<30):
    print("grade-D")
elif(num>=30 and num<50):
    print("grade-C")

elif(num>=50 and num<70):
    print("grade-b")

elif(num>=70 and num<=100):
    print("grade-A")

else:
    print("invalid")
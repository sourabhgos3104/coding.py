
salary=int(input("enter your salary:"))

if(salary>=0 and salary<=10000):
      print("your model is nokia", "its price is:5000")
      print("your 10% interest on mobile is:",(5000*10/100))
      print("your total amount on mobile is:",(5000+(5000*10/100)))
      print("your monthly installments is:",((5000+(5000*10/100))/24) )

elif(salary>10000 and salary<=50000):
       print("your model is realme","its price is:30000")
       print("your 10% interest on mobile is:",(30000*15/100))
       print("your total amount on mobile is:",(30000+(30000*15/100)))
       print("your monthly installments is:",((30000+(30000*15/100))/36) )

else:
       print("your model is iphone","its price is:80000")
       print("your 10% interest on mobile is:",(80000*20/100))
       print("your total amount on mobile is:",(80000+(80000*20/100)))
       print("your monthly installments is:",((80000+(80000*20/100))/48) )





a=int(input("enter your number:"))

if(a==1):
  print("select option 2,3,4:")
  a=int(input("enter your number:"))

  if(a==2):
     print("select option 3,4:")
     a=int(input("enter your number:"))

     if(a==3):
         print("select option 2,4")
         a=int(input("enter your number:"))

         if(a==2):
             print("select option 4")
             a=int(input("enter your number:"))
              
             if(a==4):
                 print("reached")
             else:
                 print("invalid")


         elif(a==4):
              print("reached")
         else:
             print("invalid")        

          
     elif(a==4):
         print("reached")

     else:
         print("invalid")       
     
  elif(a==3):
        print("select option 2,4:")
        a=int(input("enter your number:"))

  elif(a==4):
      print("reached")

  else:
        print("invalid")

else:
     print("invalid")

# questions= []
# questions.append("Q1:python was devloped in")
# questions.append("Q2:c++ was devloped in")
# questions.insert(2,"Q3:html was devloped in")
# questions.insert(3,"Q4:when one is not a valid keyword in python")
# questions.append("Q5:full form of css")
# questions.append("Q5:full form of css")
# questions.pop()


# options=[

# ("A:1990","B:1991","C:1999","D:2000" ),
# ("A:1991","B:1992","C:1998","D:2001" ),
# ("A:1992","B:1994","C:1998","D:2003" ),
# ("A:1998","B:1993","C:1996","D:2004" ),
# ("A:CASCADING STYLE SHEET","B:CASCADING SHEET","C:CASCADING CARD","D:CASCARDING STYLE SHEET" )

# ]

# answers =["B","C","A","A","A"]


# ans=[]
# points=0

# print(questions[0])
# print(options[0])
# ans.append(input("select the correct option:").upper())
# points=points+1 if ans[0] == answers[0] else points


# print(questions[1])
# print(options[1])
# ans.append(input("select the correct option:").upper())
# points=points+1 if ans[1] == answers[1] else points


# print(questions[2])
# print(options[2])
# ans.append(input("select the correct option:").upper())
# points=points+1 if ans[2] == answers[2] else points


# print(questions[3])
# print(options[3])
# ans.append(input("select the correct option:").upper())
# points=points+1 if ans[3] == answers[3] else points




# print(questions[4])
# print(options[4])
# ans.append(input("select the correct option:").upper())
# points=points+1 if ans[4] == answers[4] else points


# print()
# print(f" total points are: {points}")
# print(f" your selected options are: {ans}")
# print(f" the correct answers are: {answers}")





# a=10
# b=10
# print(id(a))
# print(id(b))


# a=20
# b=10

# print(id(a))
# print(id(b))

# a=10
# b=20
# print(a**2)
# print(b**2)

# li1=[101,1,2,6,8]
# li2=[101,2,5,4,8]

# print(id(li1))
# print(id(li2))



# tup=(1,2,3,4,5,6,1,7,7,8,9,4,8,9)

# print(max(tup))
# print(min(tup))
# print(type(tup))
# print(len(tup))
# print(tup[0])
# print(tup[-1])
# print(tup[4])
# print(tup.count(1))
# print(tup.count(7))


# li=[1,2,3,4,5,6,7,8,9,12,13]
# li=set(li)

# set={1,2,3,4,5,14}

# print(li)





# set={1,2,3,4,5}
# set.add(101)
# set.add("hello")
# set.add(101)
# set.pop()
# set.remove(101)
# set.discard(101)
# set.update(range(10,16))
# set.clear()
# print(set)


# s={1,2,3,5,6}
# a=s
# s.add(101)
# print(a)
# print(s)


# s={1,2,3,5,6}
# a=s.copy()
# s.add(101)
# print(a)
# print(s)


# s1={1,2,3,4,5,7}
# s2={1,2,3,4,5,6}
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))
# print(s1.symmetric_difference(s2))

# li=[1,2,3,2,4,5,6,5,8,6,5]
# li.insert(3,201)
# li.append(202)
# li.pop()
# li.remove(201)
# li.pop(8)
# print(li)


# d={100:"durga",200:"ravi",300:"shiva"}
# print(d)
# del d[100]
# print(d)
# del d[300]
# print(d)
# print(d.get(200))


# d={"name":"manoj", "age": 24}
# d.clear()
# print(len(d))
# print(d)
# print(d.get("age"))
# del d




# d={"name":"manoj", "age": [18,5,25,56,78,41]}

# d.setdefault ("grade","A")
# print(d)


# print(range(0,6))
# print(list(range(0,6)))
# print(list(range(0,6,1)))
# print(list(range(0,-8,-1)))
# print(list(range(1,11,3)))



# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# print(a) if(a>b) else print(b)



# a=int(input("enter the number:"))
# print("even") if(a%2==0) else print("odd")


# a=int(input("enter the number:"))
# print("multiple") if(a%5==0) else print("not an multiple")

# age=int(input("enter the age:"))
# print("eligible") if(age>18) else print("not eligible")

# password=int(input("enter the password:"))
# print("correct") if(password==12345) else print("not correct")



# a=int(input("enter the number:"))
# print("between") if(a>1 and a<100) else print("not in between")

# s="hello"
# print(s[0:1])
# print(s[::])
# print(s[::-1])


# s="hello"
# print(s[::-1])
# print(s[::])
# print(s[0:4])
# print(s[0::2])
# print(s[-1:1])
# print(s[-1:-5:-1])
# print(s[-1:-5:])
# print(s[0:6])

# print(s[::][0:1])????


# a=input("enter a number:")
# print (a)

# a=eval(input("enter a number:"))
# print (a)


# a=20
# b=30
# if a>b:
#     print(a)
# else:
#     print(b) 



# pin=int(input("enter the password:"))
# print("correct") if(pin==1234) else print("invalid")


# b=input("enter the character:")
# li=['a','e','i','o','u']

# if (b  in li):
#     print("vowel")
# else:
#     print("constant")



# b=input("enter the value:")
# print("vowel") if(b=='a'or b=='i' or b=='o'or b=='e' or b=='u') else print("constant")


# age=int(input("enter your age:"))
# print("eligible") if(age>18) else print("not eligible")


# num=int(input("enter your number:"))
# print("multiple") if(num%5==0) else print("not multiple")

# print("welcome to restaurant")
# print("menu:")
# menu=[
#      "1 burger : 50",
#      "2 pizza : 40",
#      "3 salad :50",
#      "4 pasta : 70",
#      "5 soda :50",

# ]
# print(menu)

# order=int(input("enter your option:"))

# if(order==1):
#     print("1 burger :50")

# elif(order==2):
#       print("2 pizza : 40")
      
# elif(order==3):
#       print("3 salad :50")

# elif(order==4):
#       print("4 pasta : 70")

      
# elif(order==5):
#       print("5 soda :50")

# else:
#       print("invalid")





# print("student grade")
# num=int(input("enter your number:"))

# if(num>=0 and num<30):
#     print("grade-D")
# elif(num>=30 and num<50):
#     print("grade-C")

# elif(num>=50 and num<70):
#     print("grade-b")

# elif(num>=70 and num<=100):
#     print("grade-A")

# else:
#     print("invalid")



# salary=int(input("enter your salary:"))

# if(salary>=0 and salary<=10000):
#       print("your model is nokia", "its price is:5000")
#       print("your 10% interest on mobile is:",(5000*10/100))
#       print("your total amount on mobile is:",(5000+(5000*10/100)))
#       print("your monthly installments is:",((5000+(5000*10/100))/24) )

# elif(salary>10000 and salary<=50000):
#        print("your model is realme","its price is:30000")
#        print("your 10% interest on mobile is:",(30000*15/100))
#        print("your total amount on mobile is:",(30000+(30000*15/100)))
#        print("your monthly installments is:",((30000+(30000*15/100))/36) )

# else:
#        print("your model is iphone","its price is:80000")
#        print("your 10% interest on mobile is:",(80000*20/100))
#        print("your total amount on mobile is:",(80000+(80000*20/100)))
#        print("your monthly installments is:",((80000+(80000*20/100))/48) )


# a=int(input("enter your number:"))

# if(a==1):
#   print("select option 2,3,4:")
#   a=int(input("enter your number:"))

#   if(a==2):
#      print("select option 3,4:")
#      a=int(input("enter your number:"))

#      if(a==3):
#          print("select option 2,4")
#          a=int(input("enter your number:"))

#          if(a==2):
#              print("select option 4")
#              a=int(input("enter your number:"))
              
#              if(a==4):
#                  print("reached")
#              else:
#                  print("invalid")


#          elif(a==4):
#               print("reached")
#          else:
#              print("invalid")        

          
#      elif(a==4):
#          print("reached")

#      else:
#          print("invalid")       
     
#   elif(a==3):
#         print("select option 2,4:")
#         a=int(input("enter your number:"))

#   elif(a==4):
#       print("reached")

#   else:
#         print("invalid")

# else:
#      print("invalid")


# #Q1
# bank=input("enter your bank:")
# if(bank=="sbi"):

#         pin=int(input("enter your pin:"))
#         if(pin==1234):
#                 print("select option -withdrawl,deposit,balance enquiry:")
#                 option=input("select your option:")

#                 if(option=="withdrawl"):
            
#                             amount=int(input("enter your withdrawl amount:"))
#                             if( amount>0 and amount<=10000):
#                                    print("your balance is:",(10000-amount))


#                             else:
#                                     print("invalid amount")
          

#                 elif(option=="deposit"):
#                         deposit=int(input("enter your deposit amount:"))

#                         if(deposit>0):
#                                 print("your balance is:",(10000+deposit))
#                         else:
#                                 print("invalid deposit")        

#                 elif(option=="balance_enquiry"):
#                         print("your current balance is:10000") 

#                 else:
#                     print("invalid option")                            
           

#         else:
#                 print("invalid pin")        
# else:
#         print("enter valid bank")             



#Q2
email=input("enter your email:")

if(email=="student@email.com"):
        password=int(input("enter your password:"))
        if(password==1234):
                print("correct")
                      
        else:
                print("incorrect")

else:
        print("invalid email")              
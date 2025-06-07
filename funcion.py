#non return without argument
#Q1
# def factorial():
#     a=int(input("enter your number:"))
#     ans=1
#     for i in range(1,a+1):
#         ans*=i
#     print(ans)    

# factorial()

#Q2
# def sum():
#     a=int(input("enter a number"))
#     sum=0
#     for i in range(1,a+1):
#         sum+=i
#     print(sum) 

# sum() 
      

#Q3
# def febonacci():
#     a=int(input("enter a number:"))
#     num1=0
#     num2=1
#     for i in range(1,a):
#         if(i<2):
#             print(num1)
#             print(num2)
#         if(i>1):    
#              num=num1+num2
#              num1=num2
#              num2=num
#              print(num)

# febonacci()

#Q4
# def cal_sum():
#     a=int(input("enter a number:"))
#     b=int(input("enter a number:"))
#     c=a+b
#     print(c)

# cal_sum()


#Q1
# def sum():
#     num1=int(input("enter your number:"))
#     num2=int(input("enter your number:"))
#     return num1+num2

# a=sum()
# print(a)


#Q2
# def fact():
#     num=int(input("enter a number:"))
#     fact=1
#     for i in range(1,num+1):
#              fact*=i
#     return fact

# a=fact()
# print(a)             


#Q3
# def square():
#     for i in range(1,11):
#         yield i*i

# a=square()
# for i in a:
#     print(i,end=" ")


#Q4
# def isprime():
#     num=int(input("enter a number:"))
#     c=0
#     for i in range(1,num+1):
#         if(num%i==0):
#             c=c+1

#     if(c==2):
#         return "prime"  

#     else:
#         return "not a prime"
    
# ans=isprime()
# print(ans) 
   

#Q5
# def perfect():
#       num=int(input("enter a number:"))
#       ans=0
#       for i in range(1,num):
#             if(num%i==0):
#                   ans=ans+i

#       if(ans==num):
#                   return "perfect number"

#       else:
#                   return "not perfect"

# c=perfect()
# print(c)                  


#Q6
# def pallindrom():
#     num=int(input("enter a number:"))
#     a=num
#     rev=0
#     while(num>0):
#         digit=num%10
#         rev=rev*10+digit
#         num//=10

#     if(rev==a):
#         return "pallindrom" 
#     else:
#         return "not pallindrom"

# ans=pallindrom()
# print(ans) 



#q1 26-05-25
# def perfect_number(num):
#     ans=0
#     for i in range(1,num):
#         if num%i==0:
#             ans+=i

#     if(ans==num):
#         print("perfect number") 

#     else:
#         print("not perfect")           

# a=int(input("enter a number"))
# perfect_number(a)

# a=int(input("enter a number"))
# perfect_number(a)

# a=int(input("enter a number"))
# perfect_number(a)


#q2
# def perfect_number():
#     num=int(input("enter a number"))
#     ans=0
#     for i in range(1,int(num**0.5)+1):
#         if num%i==0:
#             ans+=i

#     if(ans==num):
#         print("perfect number") 

#     else:
#         print("not perfect") 

# while(1):
#     a=int(input("press 1 to exit or press 2 to continue "))
#     if a==1:
#         break
#     elif a==2:
#        perfect_number()


#position argument
# def student_data(name,rollno):
#     print(f"the student_name is{name} the rollno is{rollno}")

# student_data("jatin",101)

#keyword argument
# def student_data(name,rollno):
#     print(f"the student_name is{name} the rollno is{rollno}")

# student_data(rollno=101,name="jatin")


#27-05-2025
# 3 default argument
# def sum(a,b):
#     return a+b
# sum(7,8)

#4 variable lenth argument
# def sum(*a):
#     ans=0
#     for i in a:
#        ans+=i
#     print(ans)

# sum(1,2,3,4) 
   

#5 keyword variable lenth argument
# def viewdate(**kwarg):
#     print(kwarg)

# dic={
#     "name": "rohit",
#     "rollno": 101 ,
#     "name2": "ajay",
#     "rollno1": 102,
#     "name3": "keshav",
#     "rollno2": 103
# }    

# viewdate(**dic)

#or

# def viewdate(**swarg):
#     return(swarg)
# dic={
#     "name": "rohit",
#     "rollno": 101 ,
#     "name2": "ajay",
#     "rollno1": 102,
#     "name3": "keshav",
#     "rollno2": 103
# }

# ans=viewdate(**dic)
# print(ans)


#29-05-2025  
#Q1 SQUARE OF NUMBER?
# def square(a):
#     return a*a
# print(square(5))
    

# square=lambda x:x*x
# print(square(6))

# cube=lambda x:x*x*x
# print(cube(6))

# greater=lambda x,y:x if x>y else y
# print(greater(6,9))





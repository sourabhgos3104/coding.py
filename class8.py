email=input("enter your email:")

if(email=="student@email.com"):
        password=int(input("enter your password:"))
        if(password==1234):
                print("correct")
                      
        else:
                print("incorrect")

else:
        print("invalid email")  




print("you have 3 mobile brands:- realme,iphone,oneplus")
brand=input("enter your mobile brand:")

if(brand=="realme"):
    print("select your model:- realme13 ,realme13 pro")
    model=input("enter your model name:")

    if(model=="realme13"):
            print("your realme13 price is:25,000")

    elif(model=="realme13 pro"):
            print("your realme13 pro price is:10,000") 

    else:
         print("invalid model enter") 



elif(brand=="iphone"):
        print("select your model:- iphone14, iphone15") 
        model=input("enter your model name:")

        if(model=="iphone14"):
             print("your iphone14 price is:70,000")

        elif(model=="iphone15"):
            print("your iphone15 price is:80,000") 

        else:
             print("invalid model enter")

elif(brand=="oneplus"):
    print("select your model:- oneplus nord, oneplus nord3")
    model=input("enter your model name:")

    if(model=="oneplus nord"):
             print("your oneplus nord price is:30,000")

    elif(model=="oneplus nord3"):
            print("your oneplus nord3 price is:35,000") 

    else:
             print("invalid model enter") 


else:
    print("invalid brand enter")    


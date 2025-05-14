
bank=input("enter your bank:")
if(bank=="sbi"):

        pin=int(input("enter your pin:"))
        if(pin==1234):
                print("select option -withdrawl,deposit,balance enquiry:")
                option=input("select your option:")

                if(option=="withdrawl"):
            
                            amount=int(input("enter your withdrawl amount:"))
                            if( amount>0 and amount<=10000):
                                   print("your balance is:",(10000-amount))


                            else:
                                    print("invalid amount")
          

                elif(option=="deposit"):
                        deposit=int(input("enter your deposit amount:"))

                        if(deposit>0):
                                print("your balance is:",(10000+deposit))
                        else:
                                print("invalid deposit")        

                elif(option=="balance_enquiry"):
                        print("your current balance is:10000") 

                else:
                    print("invalid option")                            
           

        else:
                print("invalid pin")        
else:
        print("enter valid bank")             

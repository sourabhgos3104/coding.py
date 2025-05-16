
unit=int(input("enter your unit:"))
if(unit>=0 and unit<=50):
    print("your per unit price is 5 rupee:")
    print("your bill is:",(unit*5))

elif(unit>50 and unit<=100):
    print("your per unit price is 5 rupee upto 50 unit:",(50*5))
    print("your per unit price above 50 unit is 10 rupee:",((unit-50)*10))
    print("your total bill amount of unit is:",((50*5)+((unit-50)*10)))    

elif(unit>100 and unit<=200):
      print("your per unit price is 5 rupee upto 50 unit:",(50*5))
      print("your per unit price of b/w 50 to 100 unit is 10 rupee:",(50*10))
      print("your per unit price above 100 unit is:",(unit-100)*20) 
      print("your total bill amount is:",((50*5)+(50*10)+(unit-100)*20))

else:
      print("your per unit price is 5 rupee upto 50 unit:",(50*5))
      print("your per unit price of b/w 50 to 100 unit is 10 rupee:",(50*10))
      print("your per unit price above 100 unit is:",(100*20)) 
      print("your per unit price above 200 unit is:",((unit-200)*30))
      print("your total bill amount is:",((50*5)+(50*10)+(100*20)+(unit-200)*30))
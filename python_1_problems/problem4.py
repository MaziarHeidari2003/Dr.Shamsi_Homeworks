income = int(input("Lets calculate the taxes, enter your income please: "))
if  income > 0 :
    if income <= 20000000:
        print(income/10)
       # print(type(income/10)) its some how interesting! it was int , but now we have float! thats atomic type convesion
    if income > 20000000 and income <= 50000000 :  
        print((income-20000000)*15/100)  
    if income > 50000000 :
        print((income-50000000)*20/100)    
        
else:
    print("Invalid value")    
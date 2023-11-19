x = int(input("Enter the number: "))
y = x/2
condtionCheck = True
if x == 0 :  #What if the user enters 0!
  print(0) 
else:  
  while condtionCheck:
    y = (y + x/y)/2
    z = (y*y) - x
    if z< 0.000001: # How accurate should this number be? Mine is close enough i think.
      condtionCheck = False
  print(y)  
    
  
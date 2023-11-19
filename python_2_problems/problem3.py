x = int(input("Enter the number: "))
y = 1
z = True
while z :
  if x == 1 or x ==0:
    print(y)
    z = False
    #break, i wasnt sure if its ok to use break keyword in this exercise
  else:  
    y *= x*(x-1) 
    x -=2




while True :
  sum = 0
  number = int(input("Enter a number: "))
  if number == 0 :
    break
  while number > 0 :
    sum += number%10
    number //=10
  print(f"The sum of digits is {sum}")  


  #one of my challenges in this code was understanding the variable scope. you give a value somewhere. you do some functions somewhere else. when you print the value of the specific variable, which value is going to be printed??????? i wnatet to use the number variable in the print. but its value was always 0 !!!
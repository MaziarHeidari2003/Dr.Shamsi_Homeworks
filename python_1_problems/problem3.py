score = -1
#while score<0 or score>20:
score = int(input("Enter the score you got: "))
if score >=0 and score <= 20 :

    if score >= 17:
        print("A")
    elif score < 17 and score >= 15 :
        print("B")        
    elif score < 15 and score >=10 :
        print("C")
    else:
        print("D")    
else:
    print("The score is invalid")
          
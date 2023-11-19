month_1 = 'Farvardin'
month_2 = 'Ordibehesht'
month_3 = 'Khordad'
month_4 = 'Tir'
month_5 = 'Mordad'
month_6 = 'Shahrivar'
month_7 = ' Mehr'
month_8 = 'Aban'
month_9 = 'Azar'
month_10 = 'Day'
month_11 = 'Bahman'
month_12 = 'Esfand'

day_of_year_int = -1
try:
    #while day_of_year_int<0 or day_of_year_int>367:
    day_of_year_int = int(input("enter the specific day of the year: "))
    if day_of_year_int > 0 and day_of_year_int < 367 : 
        
        if day_of_year_int < 32 :
            print("Day "+str(day_of_year_int)+" of "+month_1)
        elif day_of_year_int <63 :
            print("Day "+str(day_of_year_int -31)+" of "+month_2) 
        elif day_of_year_int <94 :
            print("Day "+str(day_of_year_int - 62)+" of "+month_3) 
        elif day_of_year_int <125 :
            print("Day "+str(day_of_year_int - 93)+" of "+month_4)
        elif day_of_year_int <156 :
            print("Day "+str(day_of_year_int - 124)+" of "+month_5)
        elif day_of_year_int <187 :
            print("Day "+str(day_of_year_int - 155)+" of "+month_6)
        elif day_of_year_int <217 :
            print("Day "+str(day_of_year_int - 186)+" of "+month_7)
        elif day_of_year_int <247 :
            print("Day "+str(day_of_year_int - 216)+" of "+month_8)
        elif day_of_year_int <277 :
            print("Day "+str(day_of_year_int - 246)+" of "+month_9)    
        elif day_of_year_int <307 :
            print("Day "+str(day_of_year_int - 276)+" of "+month_10)
        elif day_of_year_int <337 :
            print("Day "+str(day_of_year_int - 306)+" of "+month_11)
        elif day_of_year_int <367 :
            print("Day "+str(day_of_year_int - 336)+" of "+month_12)          
    else:
        print("Do you even know how many days a year is?! Invalid number!")         

except ValueError as e :
    print(f"Oops!There was a valueError: {e}")    
except TypeError as e:
    print(f"Whoops! There was as typeError: {e}") 
except IndexError as e:
    print(f"Dang! There was an indexError: {e}")         
except Exception as e:
    print(f"Uh oh! An unexpedted exception eccured: {e}")    
else:
    print("The code ran smoothly")    


  
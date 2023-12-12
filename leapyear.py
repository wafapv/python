current_year = int(input("Enter the current year: ")) 
final_year = int(input("Enter the final year: ")) 
if (current_year<final_year) :
   print("The leap years are:")
   for a in range(current_year,final_year+1):
     if(a%4==0):
       print(a)
else:
    print("No future leap years found")
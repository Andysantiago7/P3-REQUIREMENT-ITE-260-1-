def calculate_expenses(transportation_fare,food , academic_supply):
     total = transportation_fare + food + academic_supply
     return total

print("=============== BUDGET TRACKER ===============")
print("THIS IS YOUR BUDGET FOR MONDAY TO FRIDAY: ")

budget = int(input("ENTER YOUR BUDGET: "))
print()

total_expenses = 0

days = ["MONDAY" , "TUESDAY" ,"WEDNESDAY","THURSDAY", "FRIDAY"]

for expenses in range (1,6):
     print(f"TOTAL EXPENSES ON {days[expenses -1]}: ")
     
     transportation_fare = float(input("TRANSPORTATION: "))
     food = float(input("FOOD: "))
     academic_supply = float(input("ACADEMIC SUPPLY: "))
     total = calculate_expenses( transportation_fare, food , academic_supply)

     total_expenses += total   

     
     days_left = 5 - expenses
     remaining_budget = budget - total_expenses
     print("TOTAL:" , total)
     print("                                                                                        ")
     print("REMAINING BUDGET:", remaining_budget)

     if remaining_budget < 0:
        print("WARNING: You have exceeded your weekly budget!")

     elif days_left > 0:
        daily_allowance = remaining_budget / days_left

        print("DAYS REAMINING:", days_left)
        print("                                                                                     ")
        print("SUGGESTED SPENDING LIMIT PER DAY:",
              round(daily_allowance, 2))

     if total > budget / 5:
            print("WARNING: YOU SPENT MORE THAN YOUR AVERAGE DAILY BUDGET!")

     if daily_allowance < budget / 5:
            print("WARNING: YOU NEED TO SPEND LESS ON THE REMAINING DAYS!")
     
     print("                                                                                             ")      
     

print("==============================================")
print("                                                                    ")  
print("TOTAL EXPENSES FROM MONDAY TO FRIDAY:" , total_expenses)

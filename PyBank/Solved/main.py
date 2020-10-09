
# Modules
import os
import csv

budget_csv = os.path.join( "..","Resources", "budget_data.csv")
months = []
profits = []
total = 0
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csv_reader)
    
    for row in csv_reader:
        months.append(row[0])
        profits.append(int(row[1]))

    
  
    # The net total amount of "Profit/Losses" over the entire period
    
    

           
    # The average of the changes in "Profit/Losses" over the entire period

    # The greatest increase in profits (date and amount) over the entire period

    # The greatest decrease in losses (date and amount) over the entire period

month_count = len(months)
total = sum(profits)    
    


print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {month_count} ")
print(f"Total: ${total}")
# print(f"Average Change: ${avg_change}")
# print(f"Greatest Increase In Profits: {} (${avg_change})")
# print(f"Greatest Decrease In Profits: {} (${avg_change})")


# Modules
import os
import csv

budget_csv = os.path.join( "..","Resources", "budget_data.csv")
months = []
profits = []
monthly_change = []
total = 0
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csv_reader)
    
    for row in csv_reader:
        months.append(row[0])
        profits.append(int(row[1]))

  

    for i in range(len(profits)-1):
        monthly_change.append(profits[i+1]-profits[i])


    # The average of the changes in "Profit/Losses" over the entire period


    # The greatest increase in profits (date and amount) over the entire period

    # The greatest decrease in losses (date and amount) over the entire period

month_count = len(months)
  # The net total amount of "Profit/Losses" over the entire period
total = sum(profits)    
avg_change  = round((sum(monthly_change) / len(monthly_change)), 2)

max_inc = max(monthly_change)
max_dec = min(monthly_change)
max_inc_month = monthly_change.index(max(monthly_change)) + 1
max_dec_month = monthly_change.index(min(monthly_change)) + 1 


# Print everything
print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {month_count} ")
print(f"Total: ${total}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase In Profits: {months[max_inc_month]} (${max_inc}) ")
print(f"Greatest Decrease In Profits:{months[max_dec_month]} (${max_dec})")

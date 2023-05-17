# import the os module and module for reading csv files
import os
import csv


csvpath = os.path.join('Resources','budget_data.csv')

total_months = 0
net_profit = 0
changes_list = []
previous = 0


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
   # print(csvreader)

    csv_header = next(csvreader)
    #print(f"CVS Header: {csv_header}")

    for row in csvreader:
        total_months = total_months + 1
        net_profit = int(row[1]) + net_profit
        
        change = int(row[1]) - previous
        previous = int(row[1])
        changes_list.append(change) 
    
average_change = sum(changes_list) / len(changes_list)


print("Financial Analysis")
print("")
print("---------------------")
print("")
print(f'Total Months: ${total_months}')
print(f'Total: {"$"}{net_profit}')
print(changes_list)
print(average_change)
  

   
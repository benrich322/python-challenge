# import the os module and module for reading csv files
import os
import csv
from datetime import datetime



csvpath = os.path.join('Resources','budget_data.csv')

total_months = 0
net_profit = 0
revenue_changes = []
date_and_revenue_changes = []
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
        revenue_changes.append(change)

        date_and_revenue_elements = [row[0],change]
        date_and_revenue_changes.append(date_and_revenue_elements)


revenue_changes = revenue_changes[1:]
average_change = sum(revenue_changes) / len(revenue_changes)

max_output = max(date_and_revenue_changes, key=lambda x: x[1])
min_output = min(date_and_revenue_changes, key=lambda x: x[1])

date_time_str = max_output[0] 
date_time_obj = datetime.strptime(date_time_str, '%d-%b')
max_date_new_format = (date_time_obj.strftime("%b-%d"))

date_time_str = min_output[0]
date_time_obj = datetime.strptime(date_time_str, '%d-%b')
min_date_new_format = (date_time_obj.strftime("%b-%d"))

print_statement = (
    f'Financial Analysis\n'
    f'---------------------\n'
    f'Total Months: ${total_months}\n'
    f'Total: {"$"}{net_profit}\n'
    f'Average Change: {"$"}{round((average_change),2)}\n'
    f'Greatest Increase in Profits: {max_date_new_format} ({"$"}{max_output[1]})\n'
    f'Greatest Decrease in Profits: {min_date_new_format} ({"$"}{min_output[1]})\n'
)

print(print_statement)



   
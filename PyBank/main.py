# import the os module and module for reading csv files
import os
import csv
# import the module for date time formatting
from datetime import datetime


# identify the path of the csv file
csvpath = os.path.join('Resources','budget_data.csv')
# create the text file
PyBank_text_file = "PyBank_text_file.txt"

# create variables for loop 
total_months = 0
net_profit = 0
revenue_changes = []
date_and_revenue_changes = []
previous = 0


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:

        # counts number of months in dataset
        total_months = total_months + 1

        # sums the "Profit/Losses" over the entire period
        net_profit = int(row[1]) + net_profit

        # calcs the changes in "Profit/Losses" over the entire period
        change = int(row[1]) - previous
        previous = int(row[1])
        revenue_changes.append(change)

        # assigns the date with the change as a list, then adds it to another list
        date_and_revenue_elements = [row[0],change]
        date_and_revenue_changes.append(date_and_revenue_elements)

# creates a new list that only shows the revenue changes
revenue_changes = revenue_changes[1:]

# calculates the average of the revenue changes
average_change = sum(revenue_changes) / len(revenue_changes)

# finds the greatest inc and dec in profits (date and amount) 
max_output = max(date_and_revenue_changes, key=lambda x: x[1])
min_output = min(date_and_revenue_changes, key=lambda x: x[1])

# updates the date format of min and max
date_time_str = max_output[0] 
date_time_obj = datetime.strptime(date_time_str, '%d-%b')
max_date_new_format = (date_time_obj.strftime("%b-%d"))

date_time_str = min_output[0]
date_time_obj = datetime.strptime(date_time_str, '%d-%b')
min_date_new_format = (date_time_obj.strftime("%b-%d"))

# prints the results
print_statement = (
    f'Financial Analysis\n'
    f'---------------------\n'
    f'Total Months: {total_months}\n'
    f'Total: {"$"}{net_profit}\n'
    f'Average Change: {"$"}{round((average_change),2)}\n'
    f'Greatest Increase in Profits: {max_date_new_format} ({"$"}{max_output[1]})\n'
    f'Greatest Decrease in Profits: {min_date_new_format} ({"$"}{min_output[1]})\n'
)

print(print_statement)

# exports a test file of the results
with open(PyBank_text_file, "w") as text_file:
    text_file.write(print_statement)



   
# import the os module and module for reading csv files
import os
import csv
# import the module for date time formatting
from datetime import datetime


# identify the path of the csv file
csvpath = os.path.join('Resources','election_data.csv')
# create the text file
PyPoll_text_file = "PyPoll_text_file.txt"

# create variables for loop 
total_votes = 0



with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:

        # counts number of months in dataset
        total_votes = total_votes + 1


# prints the results
print_statement = (
    f'Election Results\n'
    f'---------------------\n'
    f'Total Votes: {total_votes}\n'
    f'---------------------\n'
    f'---------------------\n'
    f'---------------------\n'
)

print(print_statement)

# exports a test file of the results
with open(PyPoll_text_file, "w") as text_file:
    text_file.write(print_statement)



   
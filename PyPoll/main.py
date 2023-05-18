# import the os module and module for reading csv files
import os
import csv
# import the module for date time formatting
from datetime import datetime
import operator


# identify the path of the csv file
csvpath = os.path.join('Resources','election_data.csv')
 
# create the text file
PyPoll_text_file = "PyPoll_text_file.txt"

# create variables for loop 
total_votes = 0
candidates = []
change = ''
previous = change
candidate_vote_count = 0

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
   

    csvreader = sorted(csvreader, key=operator.itemgetter(2)) 

    # Read the header row first
    #csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:

        total_votes = total_votes + 1
        candidate_vote_count = candidate_vote_count + 1
        previous = change
        change = row[2]
         # calcs the changes in "Profit/Losses" over the entire period
        if change != previous:
            list_test = [previous,candidate_vote_count]
            candidates.append(list_test)
            candidate_vote_count = 0
        else:
           previous = change
    
    list_test = [previous,candidate_vote_count + 1]
    candidates.append(list_test)
            

# creates a new list that only shows the candidates
candidate_results = candidates[1:]



# finds the greatest inc and dec in profits (date and amount) 
max_output = max(candidate_results, key=lambda x: x[1])

result_list = []

for x in candidate_results:

    x = f'{x[0]}: {"{0:.3%}".format(x[1]/total_votes)} ({x[1]})'
    result_list.append(x)


print_statement = (

    f'\nElection Results\n'
    f'\n---------------------\n'
    f'\nTotal Votes: {total_votes}\n'
    f'\n---------------------\n'
    f'\n{result_list[0]}\n'
    f'{result_list[1]}\n'
    f'{result_list[2]}\n'
    f'\n---------------------\n'
    f'\nWinner: {max_output[0]}\n'
    f'\n---------------------\n'
)

print(print_statement)

#exports a test file of the results
with open(PyPoll_text_file, "w") as text_file:
    text_file.write(print_statement)



   
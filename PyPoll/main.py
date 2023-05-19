# import the os module and module for reading csv files
import os
import csv
# import the module for sorting
import operator


# identify the path of the csv file
csvpath = os.path.join('PyPoll','Resources','election_data.csv')
 
# create the text file
output_path = os.path.join('PyPoll','analysis','PyPoll_text_file.txt')

# create variables for loop 
total_votes = 0
candidates = []
canidate_name = ''
previous_candidate = canidate_name
candidate_vote_count = 0

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
   
    # sort the csv file by candidate
    csvreader = sorted(csvreader, key=operator.itemgetter(2)) 

    # Read each row of data after the header
    for row in csvreader:

        # sums the total votes
        total_votes = total_votes + 1
        # sums the votes by candidate
        candidate_vote_count = candidate_vote_count + 1
        # candidate name from previous row
        previous_candidate = canidate_name
        # candidate name from current row
        canidate_name = row[2]
        # if current row candidate doesn't equal previous candidate...
        if canidate_name != previous_candidate:
            # add candidate and vote count to list
            list_test = [previous_candidate,candidate_vote_count]
            candidates.append(list_test)
            # resets the vote count
            candidate_vote_count = 0
        else:
           previous_candidate = canidate_name

    # adds the last candidate from csv file to the list. Adds 1 to include the last row in the vote count
    list_test = [previous_candidate,candidate_vote_count + 1]
    candidates.append(list_test)

# creates a new list that only shows the candidates
candidate_results = candidates[1:]

# finds the candidate with the most votes
max_output = max(candidate_results, key=lambda x: x[1])

# new list for print statement
result_list = []

# read each element in the candidate_results list
for x in candidate_results:

    # formats a list for the print statement
    x = f'{x[0]}: {"{0:.3%}".format(x[1]/total_votes)} ({x[1]})'
    result_list.append(x)

# print statement
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
with open(output_path, "w") as text_file:
    text_file.write(print_statement)



   
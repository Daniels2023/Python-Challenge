#importing libraries
import os
import csv

#creating variables to save the file path
input_csvpath = os.path.join('Resources','election_data.csv')
output_txtpath = os.path.join('Analysis','analysis_election.txt')

#Creating a dictionary to store candidates and votes
candidates = {}

#using with statement to read and write in the file
with open(input_csvpath) as input_file:
    
    #variable for reading
    csvreader = csv.reader(input_file, delimiter=',')
    
    #skiping the header and creating a variable to store Total Votes
    next(csvreader)
    totalVotes = 0
    #Looping through the data and adding 1 vote per row
    for row in csvreader:
        totalVotes +=1
        #Creating a variable and storing the candidate name
        candidate_name = row[2]
        #Checking if candidate is in the dictionary and adding votes to the candidate name
        if candidate_name not in candidates:
            candidates[candidate_name] = 1
        else:
            candidates[candidate_name] +=1
    #Printing the Total Votes
    print(f'Election Results\n-------------------------\nTotal Votes: {totalVotes}\n-------------------------')
    #Looping through candidates and printing the candidate, percentage and total votes
    winnerNumber = 0
    for candidate in candidates:
        print(f'{candidate}: {round((candidates[candidate]/totalVotes)*100,2)}% {candidates[candidate]}')
        #Checking for the winner
        if candidates[candidate] > winnerNumber:
            winnerNumber = candidates[candidate]
            winner = candidate
    #Printing the winner
    print(f'-------------------------\nWinner: {winner}\n-------------------------')

#Creating a .txt Analysis file with the results
with open(output_txtpath, 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {totalVotes}\n")
    output_file.write("-------------------------\n")
    for candidate in candidates:
        output_file.write(f"{candidate}: {round((candidates[candidate]/totalVotes)*100,2)}% ({candidates[candidate]})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")
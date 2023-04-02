Financial Analysis

The objective of this code is to read a CSV file that contains financial data from Jan-10 to Feb-17 and output a summary report of the data in the CSV file. The summary report includes:
Total number of months included in the dataset.
Total amount of "Profit/Losses" over the entire period.
Average of the changes in "Profit/Losses" over the entire period.
Greatest increase in profits (date and amount) over the entire period.
Greatest decrease in losses (date and amount) over the entire period.

Code Summary

This code first imports the necessary libraries, os and csv. It then creates variables to store the file paths of the input and output files.
Next, it creates an empty dictionary to store the difference between consecutive months' profits/losses. The code reads the CSV file using a with statement and csv.reader, and skips the header of the file. The variables that are going to be used in the loop are then initialized. A for loop is used to go through each row in the CSV file, and it adds 1 to the total number of months and adds the profit/loss to the total value.
For each row, the difference between the current month's profit/loss and the previous month's profit/loss is calculated, and it is stored in the difference dictionary. The greatest increase and decrease in profits are also stored, along with their respective months. Finally, the average change is calculated.
The results are then printed in the terminal and a new .txt file is created in the Analysis folder with the same results.

Election Analysis

The objective of this code is to read a CSV file that contains data for a local election and output a summary report of the data in the CSV file. The summary report includes:
Total number of votes.
A complete list of candidates who received votes.
Percentage of votes for each candidate.
Total number of votes for each candidate.
The winner of the election.

Code Summary

This code first imports the necessary libraries, os and csv. It then creates variables to store the file paths of the input and output files.
Next, it creates an empty dictionary to store the candidates and their respective votes. The code reads the CSV file using a with statement and csv.reader, and skips the header of the file. A for loop is used to go through each row in the CSV file and adds 1 to the total number of votes. It then checks if the candidate's name is in the dictionary, and adds a vote to their total if it is, or creates a new entry with 1 vote if it is not.
The results are then printed in the terminal, including the total number of votes, the percentage of votes and the total number of votes each candidate received, and the winner of the election based on the popular vote. A new .txt file is also created in the Analysis folder with the same results.

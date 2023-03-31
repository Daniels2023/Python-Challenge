#Importing libraries
import os
import csv

#Creating variables to store file path
csvpath_input = os.path.join('Resources','budget_data.csv')
txtpath_output = os.path.join('Analysis','Financial_analysis.txt')

diference = {}

#Reading the csv file using with statement
with open(csvpath_input) as input_file:
    csvreader = csv.reader(input_file, delimiter=",")
    #Skipping the header and creating all variables that is going to be used on for loop
    next(csvreader)
    months = 0
    totalValue = 0
    valueNow = 0
    change = 0
    GIncrease = 0
    incMonth = ''
    GDecrease = 0
    decMonth = ''
    totalChange = 0
    #Loop to go through all the calculations starting with total months and total value
    for row in csvreader:
        months +=1
        totalValue += float(row[1])
        #Jumping the first row analysis as valueNow variable was declared as 0
        #Storing the first profit value in the variable valueNow at the end of the loop
        #In the second row loop the valueNow variable is now the previous profit value
        if valueNow != 0:
            #Storing the diference between the actual profit value with the previous one
            change = float(row[1]) - valueNow
            #Storing all diferences in a totalChange variable and saving each one in the diference Dictionary
            totalChange += change
            diference[row[0]] = change
            #Checking if the change is the greatest one and recording that month
            if change > GIncrease:
                GIncrease = change
                incMonth = row[0]
            #Checking if the change is the lowest one and recording that month
            elif change < GDecrease:
                GDecrease = change
                decMonth = row[0]
        valueNow = float(row[1])
    #Calculating the average change    
    average_change = totalChange / (months - 1)

    #printing the results in the Terminal
    print('Financial Analysis\n-------------------------\n')
    print(f'Total Months: {months}')
    print(f'Total: ${totalValue:.0f}')
    print(f'Average Change: ${average_change:.2f}')
    print(f'Greatest Increase in Profits: {incMonth} ${GIncrease:.0f}')
    print(f'Greatest Decrease in Profits: {decMonth} ${GDecrease:.0f}')

    #Creating a .txt Analysis file with the results
with open(txtpath_output, 'w') as output_file:
    output_file.write('Financial Analysis\n-------------------------\n')
    output_file.write(f'Total Months: {months}\n')
    output_file.write(f'Total: ${totalValue:.0f}\n')
    output_file.write(f'Average Change: ${average_change:.2f}\n')
    output_file.write(f'Greatest Increase in Profits: {incMonth} ${GIncrease:.0f}\n')
    output_file.write(f'Greatest Decrease in Profits: {decMonth} ${GDecrease:.0f}\n')
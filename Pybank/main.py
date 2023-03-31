import os
import csv
#from pathlib import Path

#csvpath = Path('budget_data.csv')
csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    print(csvreader)
import os
import csv

# Read csv file
budget_data = os.path.join("python-challenge","pybank","Resources", "budget_data.csv")

with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvreader = next(csvreader)

# define variables
    profit = []
    months = []
    
    for rows in csvreader:
        print(rows)
        profit.append(int(rows[1]))
        months.append(rows[0])

    

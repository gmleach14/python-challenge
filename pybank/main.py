import os
import csv

# Read csv file
budget_data = os.path.join("python-challenge","pybank","Resources", "budget_data.csv")

with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    # define variables
    profit = []
    months = 0
    change = []


    for rows in csvreader:
        profit.append(int(rows[1]))
        months += 1


    for i in range(len(profit)-1):

        change.append(profit[i+1]-profit[i])

    greatest_inc = max(change)
    greatest_dec = min(change)   
    avg_change = sum(change) / len(change)

analysis = os.path.join("python-challenge","pybank","Analysis", "pybank_analysis.csv")

with open(analysis, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")

    csvwriter.writerow(["Financial Analysis"])

    csvwriter.writerow(["----------------------------------"])

    csvwriter.writerow(["Total Months: " + str(months)])

    csvwriter.writerow(["Total Profit: $" + str(sum(profit))])

    csvwriter.writerow(["Average Change: $" + str(avg_change)])

    csvwriter.writerow(["Greatest Increase in Profits: $" + str(greatest_inc)])

    csvwriter.writerow(["Greatest Decrease in Profits: $" + str(greatest_dec)])


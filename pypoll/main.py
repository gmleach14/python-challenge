import os
import csv

# Read csv file
election_data = os.path.join("python-challenge","pypoll","Resources", "election_data.csv")

# open election_data
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    # define variables
    total_votes = 0
    candidates = []
    num_votes = []
    percent_votes = []

    for row in csvreader:
        total_votes +=1
        
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1

    for votes in num_votes:
        percentage = (votes/total_votes) 
        percentage = "{:.0%}".format(percentage)
        percent_votes.append(percentage)

    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

analysis = os.path.join("python-challenge","pypoll","Analysis", "analysis.csv")

with open(analysis, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")

    csvwriter.writerow(["Election Results"])

    csvwriter.writerow(["----------------------------------"])

    csvwriter.writerow(["Total Votes: " + str(total_votes)])

    csvwriter.writerow(["----------------------------------"])

    csvwriter.writerow([f"{candidates[0]}: {str(percent_votes[0])} ({str(num_votes[0])})"])

    csvwriter.writerow([f"{candidates[1]}: {str(percent_votes[1])} ({str(num_votes[1])})"])

    csvwriter.writerow([f"{candidates[2]}: {str(percent_votes[2])} ({str(num_votes[2])})"])

    csvwriter.writerow([f"{candidates[3]}: {str(percent_votes[3])} ({str(num_votes[3])})"])

    csvwriter.writerow(["----------------------------------"])

    csvwriter.writerow(["Winner: " + str(winning_candidate)])

    csvwriter.writerow(["----------------------------------"])
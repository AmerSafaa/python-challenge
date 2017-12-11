# Modules
import os
import csv

# Initiate the variable to rerun program on another file
more_calculations ='y'

while more_calculations == 'y':
 
  # Collects the user's input for the file to be used for running the relevant calculations
  filename = input("What is the name of the file you want to use for calculating poll results? (please remember to include the file extension) ")

  # creates the path for the relevant file
  poll_csv = os.path.join("raw_data", filename)

  # open and read csv
  with open(poll_csv, newline="") as csvfile:
       csvreader = csv.reader(csvfile, delimiter=",")

  # Skip the first row in csv
  next(csv_reader, None)


# The total number of votes cast
voters = len(open(csvreader).readline())

# A complete list of candidates who received votes and number of votes won per candidate
candidates_vote = df.groupby('Candidate').count()

# The percentage of votes each candidate won
percent_votes = 100*candidates_vote/voters

# The winner of the election based on popular vote
winner_votes = max(x[candidates_vote] for x in candidates_vote)
winner= (candidate[winner_votes])

# Printing the results of Election Polls

print("------------------")
print("Election Results")
print("------------------")
print("Total Votes: " + str(total_votes))
print("------------------")
print("Candidate Name  " + "Percent of votes  " + "Number of votes")
print(str(Candidate) + "    " + str(percent_votes) + "   " + str(candidates_vote))
print("------------------")
print("Winner: " + str(winner))
print("------------------")

more_calculations = input("Would you like to summarize other election results? (y)es or (n)o. ")

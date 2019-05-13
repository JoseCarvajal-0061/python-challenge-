import os 
import csv

Poll_csv = os.path.join("PyPoll", "election_data.csv")

with open(Poll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimeter = ",")
    csvheader = next(csvfile)

total_votes= 0 
max_votes = 0 
candidate_names = []
candidate_votes = []

winner = []
percentage = 0 
            
for row in csvreader:
    total_votes = total_votes + 1 

    candidate = row[2]
    
    if candidate not in candidate_names:
        candidate_names.append(candidate)
        candidate_votes[candidate] = 0
        candidate_votes[candidate] = candidate_votes[candidate] + 1 

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > 0):
            max_votes = votes
            winner = candidate


print(f"\n\nElection Results\n")
print(f"-------------------------\n")
print(f"Total Votes: {total_votes}\n")
print(f"-------------------------\n")


print(f"{candidate}: {percentage:.3f}% ({votes})\n")

print(f"-------------------------\n")
print("Winner: {winner[]}\n")
print(f"-------------------------\n")
# Modules
import os
import csv

election_csv = os.path.join( "..","Resources", "election_data.csv")
voter = []
candidates = []
counties = []

total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csv_reader)
    
    for row in csv_reader:
        voter.append(row[0])
        candidates.append(row[2])
        counties.append(row[1])
        if row[2] == "Khan":
            khan_votes += 1
        elif row[2] == "Correy":
            correy_votes += 1
        elif row[2] == "Li":
            li_votes += 1
        elif row[2] == "O'Tooley":
            otooley_votes += 1
    

total_votes = len(voter)
khan_pc = round((khan_votes / total_votes) * 100, 3)
correy_pc = round((correy_votes / total_votes) * 100, 3)
li_pc = round((li_votes / total_votes) * 100, 3)
otooley_pc = round((otooley_votes / total_votes) * 100, 3)



        

#   * A complete list of candidates who received votes

#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

# candidates = ["Khan", "Correy", "Li","O'Tooley"]
# votes = [khan_votes, correy_votes, li_votes, otooley_votes]

votes_dict = {"Khan": khan_votes, "Correy": correy_votes, "Li": li_votes, "O'Tooley": otooley_votes}


winner = max(votes_dict, key=votes_dict.get)

print("Election Results")
print("------------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------------")
print(f"Khan: {khan_pc}% ({khan_votes})")
print(f"Correy: {correy_pc}% ({correy_votes})")
print(f"Li: {li_pc}% ({li_votes})")
print(f"O'Tooley: {otooley_pc}% ({otooley_votes})")
print("------------------------------")
print(f"Winner: {winner}")
print("------------------------------")


# write CSV

# Specify the file to write to
output_path = os.path.join("..", "Analysis", "PyPoll Results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['-------------------------------'])
    csvwriter.writerow([f'Total Votes: {total_votes} '])
    csvwriter.writerow(['-------------------------------'])
    csvwriter.writerow([f'Khan: {khan_pc}% ({khan_votes})'])
    csvwriter.writerow([f'Correy: {correy_pc}% ({correy_votes})'])
    csvwriter.writerow([f'Li: {li_pc}% ({li_votes})']) 
    csvwriter.writerow([f"O'Tooley: {otooley_pc}% ({otooley_votes})"]) 
    csvwriter.writerow(['-------------------------------'])
    csvwriter.writerow([f'Winner: {winner}']) 
    csvwriter.writerow(['-------------------------------'])
   
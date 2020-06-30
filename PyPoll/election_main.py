import os
import csv

inpath = os.path.join('Resources/election_data.csv')
outpath = os.path.join('Analysis/election_output.txt')

inpath

votes = 0
cand_votes = 0
cand_vote_d = {}
cand_vote_per = {}
winner = ""
vote_per = {}

with open(inpath,'r') as election_d:
    csvreader = csv.reader(election_d,delimiter=',')
    csvheader = next(csvreader)
    
    for row in csvreader:
        if row[2] in cand_vote_d:
            cand_vote_d[row[2]] += 1
        else:
            cand_vote_d[row[2]] = 1
        
        votes = votes + 1
        winner = max(cand_vote_d, key=cand_vote_d.get) 

for key in cand_vote_d.keys():
    vote_l = []
    vote_l.append(cand_vote_d[key]/votes *100)
    vote_l.append(cand_vote_d[key])
    vote_per[key] = vote_l
    
print("Election Results")
print("--------------------------")
print(f"Total Votes: {votes}")
print("--------------------------")
for key in vote_per:
    print(f"{key}: {vote_per[key][0]}% ({vote_per[key][1]})")
print("--------------------------")
print(f"Winner: {winner}")

outpath

with open(outpath,'w') as txt_file:
    txt_file.write("Election Results")
    txt_file.write("\n--------------------------")
    txt_file.write(f"\nTotal Votes: {votes}")
    txt_file.write("\n--------------------------")
    for key in vote_per:
        txt_file.write(f"\n{key}: {vote_per[key][0]}% ({vote_per[key][1]})")
    txt_file.write("\n--------------------------") 
    txt_file.write(f"\nWinner: {winner}")
import os
import csv
from typing import Counter

csvpath = os.path.join('Resources', 'election_data.csv')

#Define total votes and cadidate list variables to write to
total_votes = []
candidate_list = []

#Read in election_data.csv
with open(csvpath, encoding= 'utf-8') as election_csv:

        csvreader = csv.reader(election_csv, delimiter = ',')
        csv_header = next(csvreader)

        #Count total votes in total_votes and write unique candidate to candidate_list
        for row in csvreader:
            total_votes.append((row[0]))

            if row[2] not in candidate_list:
                   candidate_list.append(row[2])
        
        #Checking to make sure above worked
        print(len(total_votes))
        print(candidate_list)


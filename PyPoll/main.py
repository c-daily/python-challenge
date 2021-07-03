import os
import csv
from typing import Counter

csvpath = os.path.join('Resources', 'election_data.csv')

#Define total votes and cadidate list variables to write to
total_votes = 0
candidate_list = []
counted_votes = []

#Read in election_data.csv
with open(csvpath, encoding= 'utf-8') as election_csv:

        csvreader = csv.reader(election_csv, delimiter = ',')
        csv_header = next(csvreader)

        #Count total votes in total_votes and write unique candidate to candidate_list
        for row in csvreader:
            total_votes = total_votes + 1

            unique_candidate = row[2]

            if unique_candidate not in candidate_list:
                candidate_list.append(unique_candidate)
                counted_votes.append(1)

            else:
                candidate_index = candidate_list.index(unique_candidate)
                
                   
        


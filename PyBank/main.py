import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

monthly_total = []
profit = []
monthly_change = []

with open(csvpath, encoding = 'utf-8') as budget_csv:

    csvreader = csv.reader(budget_csv, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        monthly_total.append(row[0])
        profit.append(int(row[1]))

    
    for i in range(len(monthly_total)-1):
        monthly_change.append(profit[i+1]-profit[i])
    
max_profit_increase = max(monthly_change)
max_profit_decrease = min(monthly_change)
max_profit_month = monthly_change.index(max(monthly_change)) + 1
min_profit_month = monthly_change.index(min(monthly_change)) + 1 

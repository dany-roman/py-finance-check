import os
import csv
csvpath = os.path.join('..','Test Data','budget_data.csv')

months = []
profloss = []
momchange = []

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    prev_row = 0
    delta = 0

    for row in csvreader:
        months.append(str(row[0]))
        profloss.append(int(row[1]))  
        delta = int(row[1]) - prev_row
        momchange.append(delta)
        prev_row = int(row[1])
    
    momchange[0] = 0
    nmonth = len(months)
    nettotal = sum(profloss)
    avgchange = round((sum(momchange) / nmonth), 2)
    maxchange = max(momchange)
    minchange = min(momchange)

print("------------------------------------------")
print("Financial Analysis")
print("------------------------------------------")
print(f'Total Months: {nmonth}')
print(f'Net Total: ${nettotal}')
print(f'Avg. Change: ${avgchange}')
print(f'Greatest Increase in Profit: ${maxchange}')
print(f'Greatest Decrease in Profit: ${minchange}')
print("------------------------------------------")
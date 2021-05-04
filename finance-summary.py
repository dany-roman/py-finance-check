# import os and csv modules
import os
import csv

# create a reference to the budget data file
csvpath = os.path.join('Test','budget_data.csv')

# create lists to hold month, profit/loss, and month over month change values
months = []
profloss = []
momchange = []

# open the budget data file 
with open(csvpath) as csvfile:

# CSV reader identifies the comma separator for easier read
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# set the first previous row and delta values to zero 
    prev_row = 0
    delta = 0

# loop through the rows and collect information as lists
    for row in csvreader:
        months.append(str(row[0]))
        profloss.append(int(row[1]))  
        delta = int(row[1]) - prev_row
        momchange.append(delta)
        prev_row = int(row[1])

# calculate the number of months, net total, average change, greatest profit increase, greatest profit decrease    
momchange[0] = 0
nmonth = len(months)
nettotal = sum(profloss)
avgchange = round((sum(momchange) / nmonth), 2)
maxchange = max(momchange)
minchange = min(momchange)

# display financial summary on terminal
print("------------------------------------------")
print("Financial Analysis")
print("------------------------------------------")
print(f'Total Months: {nmonth}')
print(f'Net Total: ${nettotal}')
print(f'Avg. Change: ${avgchange}')
print(f'Greatest Increase in Profit: ${maxchange}')
print(f'Greatest Decrease in Profit: ${minchange}')
print("------------------------------------------")

# create an financial summary file and write the findings into it. Close at the end
with open("FinancialSummary.txt", "w+") as output:

    print("------------------------------------------", file=output)
    print("Financial Analysis", file=output)
    print("------------------------------------------", file=output)
    print(f'Total Months: {nmonth}', file=output)
    print(f'Net Total: ${nettotal}', file=output)
    print(f'Avg. Change: ${avgchange}', file=output)
    print(f'Greatest Increase in Profit: ${maxchange}', file=output)
    print(f'Greatest Decrease in Profit: ${minchange}', file=output)
    print("------------------------------------------", file=output)

output.close()
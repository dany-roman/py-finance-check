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

    print("------------------------------------------")
    print("Test")
    print("------------------------------------------")
    
    prev_row = 0
    for row in csvreader:
        months.append(row[0])
        profloss.append(row[1])
        delta = int(row[1]) - prev_row
        momchange.append(delta)
        prev_row = int(row[1])
        
    print("------------------------------------------") 
    print("Months")
    print("------------------------------------------")
    print(months)
    print("------------------------------------------")
    print("Mom")
    print("------------------------------------------")
    print(momchange)

    # months = [months.append(row[0]) for row in csvreader]

    # print(months)

    # nmonth = [len(nmonth.append(row[0]) for row[0] in csvreader)]

    # print(nmonth)
# nettotal = sum(row[1] for row in csv_header)
# grincrease = csvreader['delta'].max()
# grdecrease = csvreader['delta'].min()

# prev_row = 0

# for row in csvreader:
#     delta = row[2] - prev_row
#     csvreader.append(delta)
#     prev_row = row[0]

print("------------------------------------------")
print("Financial Analysis")
print("------------------------------------------")
# print(f'Total Months: {nmonth}')
# print(f'Net Total: ${nettotal}')
#print(f'Avg. Change: ${avgchange}')
# print(f'Greatest Increase in Profit: ${grincrease}')
# print(f'Greatest Decrease in Profit: ${grdecrease}')
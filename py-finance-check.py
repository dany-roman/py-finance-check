import pandas as pd

df = pd.read_csv (r'C:\Users\Doc\Repositories\py-finance-check\Test Data\budget_data.csv')

print (df)

nmonth = df['Date']
nettotal = df['Profit/Losses'].sum()
grincrease = df['Profit/Losses'].max()
grdecrease = df['Profit/Losses'].min()

# df.insert(2, "MoM Change", "")

# df['MoM Change'] = df.Profit/Losses.diff()
# print(df)



print("------------------------------------------")
print("Financial Analysis")
print("------------------------------------------")
print(f'Total Months: {len(nmonth)}')
print(f'Net Total: ${nettotal}')
#print(f'Avg. Change: ${avgchange}')
print(f'Greatest Increase in Profit: ${grincrease}')
print(f'Greatest Decrease in Profit: ${grdecrease}')
# read excel file from datas folder and print top 5 rows
import pandas as pd

# data = pd.read_excel('datas/online_retail_II.xlsx')

# print(data.head())

##step 2---------------

# i want to read sheet1 and sheet2 from excel file then merge them and print top 5 rows
sheet1 = pd.read_excel('datas/online_retail_II.xlsx', sheet_name='Year 2009-2010')
sheet2 = pd.read_excel('datas/online_retail_II.xlsx', sheet_name='Year 2010-2011')

merged_data = pd.concat([sheet1, sheet2])

# print(merged_data.head())

# save to merged_data to new excel file
# print("Saving to excel file...")
# merged_data.to_excel('datas/merged_data.xlsx', index=False)

# save merged_data to csv file
print("Saving to csv file...")
merged_data.to_csv('datas/merged_data.csv', index=False)
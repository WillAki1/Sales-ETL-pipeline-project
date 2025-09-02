import pandas as pd
import datetime as dt
import sqlite3
# Load tide CSV file
df_tide = pd.read_csv('anonymised_tide.csv')
print(df_tide)
# This puts the code into data that is simple and readable

# Date, Amount, Payment Type, Channel, Transaction Type
df_tide = df_tide.rename(columns={
    'Paid in': 'Amount',
})
# df_tide = df_tide.append('channel')#

df_tide['Channel'] = 'Tide'
df_tide['Amount'] = pd.to_numeric(df_tide['Amount'])
# DROP Transaction description, Paid out, From, To, Transaction ID, Reference, Category name, Status, Initiated by
df_tide = df_tide.drop(columns=['Transaction description',
                                'From',
                                'Category name',
                                'To',
                                'Paid out',])
# From adding the drop.columns module, This enables me to drop the names from the data
# Therefore, not showing on the list
print(df_tide.columns)


df_tide['Date'] = pd.to_datetime(df_tide['Date'], errors='coerce')
df_tide['Date'] = df_tide['Date'].dt.strftime('%d-%m-%y')
# dt.strftime('%d-%m-%y') organises the datetime in the format I want it

print(df_tide['Date'].dtypes)
print(df_tide.head(5))
# (df_tide.head(5)) the number shows me a preview of the first 5 transactions of the data
df_tide.to_csv('AweKidsSales_Tide_Bank_Statements23_25.csv', index=False)

# AweKidsSales_Tide_Bank_Statements23_25.csv - Name of the cleaned csv file
# Index = false - prevents panda from writing the DataFrame's index as an extra column

conn = sqlite3.connect('AweKidsSales_Tide_Bank_Statements23_25.db')
df_tide.to_sql('tide_transactions', conn, if_exists='replace', index=False)
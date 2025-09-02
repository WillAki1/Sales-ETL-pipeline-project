import pandas as pd
import datetime as dt
import sqlite3
# Load square 24 CVS file
df_square24 = pd.read_csv('anonymised_square_2024.csv')
print (df_square24)
# This puts the code into data that is simple and readable

# STANDARD Date, Amount, Payment Type, Channel, Transaction Type
# THINK what would the business need

df_square24 = df_square24.rename(columns={
    'Transaction date': 'Date',
    'Transaction amount': 'Amount',
})

# DROP Address, Cashback amount, Gratuity amount, Source, Card Machine Serial No., Card Machine Name	Card Machine ID
# DROP Refund Reason, Notes, Cardholder Currency, Cardholder Amount,	Exchange rate

df_Square24 = df_square24.drop(columns=[
    'Address',
    'Cashback amount',
    'Gratuity amount',
    'Source',
    'Card Machine Serial No.',
    'Card Machine Name',
    'Card Machine ID',
    'Cardholder Currency',
    'Cardholder Amount',
    'Exchange Rate',
    ])
print(df_square24.columns)

df_square24['Date'] = pd.to_datetime(df_square24['Date'], errors='coerce')
df_square24['Date'] = df_square24['Date'].dt.strftime('%d-%m-%y')

df_square24['Channel'] = 'Square24'
df_square24['Amount'] = pd.to_numeric(df_Square24['Amount'])

print(df_square24['Date'].dtypes)
print(df_square24.head(10))

conn = sqlite3.connect('AweKidsSales_Square24_Statements23_25.db')
df_square24.to_sql('tide_transactions', conn, if_exists='replace', index=False)
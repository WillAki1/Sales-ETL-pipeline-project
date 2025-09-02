import pandas as pd
import datetime as dt
import sqlite3
# Load square 25 CVS file
df_square25 = pd.read_csv('anonymised_square_2025.csv')
print(df_square25)
# This puts the code into data that is simple and readable

# STANDARD Date, Amount, Payment Type, Channel, Transaction Type
# THINK what would the business need

df_square25 = df_square25.rename(columns={
    'Transaction date': 'Date',
    'Transaction amount': 'Amount',
})

# DROP Address, Cashback amount, Gratuity amount, Source, Card Machine Serial No., Card Machine Name	Card Machine ID
# DROP Refund Reason, Notes, Cardholder Currency, Cardholder Amount,	Exchange rate

df_Square25 = df_square25.drop(columns=[
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
print(df_square25.columns)

df_square25['Date'] = pd.to_datetime(df_square25['Date'], errors='coerce')
df_square25['Date'] = df_square25['Date'].dt.strftime('%d-%m-%y')

df_square25['Channel'] = 'Square25'
df_square25['Amount'] = pd.to_numeric(df_square25['Amount'])

print(df_square25['Date'].dtypes)
print(df_square25.head(10))

conn = sqlite3.connect('AweKidsSales_Square25_Statements24_25.db')
df_square25.to_sql('tide_transactions', conn, if_exists='replace', index=False)
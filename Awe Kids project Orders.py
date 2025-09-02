import pandas as pd
import datetime as dt
import sqlite3
# Load orders 25 CVS file
df_orders = pd.read_csv('anonymised_orders_export.csv')
print(df_orders)
# This puts the code into data that is simple and readable

df_orders = df_orders.rename(columns={
    'Paid at': 'Date',
    'Total': 'Amount',
    'Fulfilled at': 'Fulfillment Date',
})

df_orders['Channel'] = 'Shopify'
df_orders['Transaction type'] = 'Transaction Type'

df_orders['Amount'] = pd.to_numeric(df_orders['Amount'])

# DROP Fulfillment Status, Currency, Taxes, Shipping Method, Lineitem compare at price, Lineitem fulfillment status, Cancelled at, Refunded Amount, Outstanding Balance,	Location

# DROP Lineitem discount, Tax 1 Name	Tax 1 Value	Tax 2 Name	Tax 2 Value	Tax 3 Name	Tax 3 Value	Tax 4 Name	Tax 4 Value	Tax 5 Name	Tax 5 Value, Payment Terms Name, Next Payment Due At

df_orders = df_orders.drop(columns=[
    'Taxes',
    'Lineitem compare at price',
    'Cancelled at',
    'Refunded Amount',
    'Outstanding Balance',
    'Location',
    'Lineitem discount',
    'Tax 1 Name',
    'Tax 1 Value',
    'Tax 2 Name',
    'Tax 2 Value',
    'Tax 3 Name',
    'Tax 3 Value',
    'Tax 4 Name',
    'Tax 4 Value',
    'Tax 5 Name',
    'Tax 5 Value',
    'Payment Terms Name',
    'Next Payment Due At',])
print(df_orders.columns)

import datetime as dt
df_orders['Date'] = pd.to_datetime(df_orders['Date'], errors='coerce')
df_orders['Date'] = df_orders['Date'].dt.strftime('%d-%m-%y')

# dt.strftime('%d-%m-%y') organises the datetime in the format I want it
print(df_orders['Date'].dtypes)
print(df_orders.head(8))
df_orders.to_csv('AweKidsSales_Shopify_Transaction_Statements23_25.csv', index=False)

conn = sqlite3.connect('AweKidsSales_shopify_Transaction_Statements23_25.db')
df_orders.to_sql('tide_transactions', conn, if_exists='replace', index=False)
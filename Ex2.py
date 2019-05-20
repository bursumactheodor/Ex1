import numpy as np
import pandas as pd
import sqlite3

with sqlite3.connect('db.sqlite3') as conn:
    #pd.to_sql('utilizatori_users', conn)
    df=pd.read_sql_query("SELECT * from utilizatori_users", conn)

    df['FullName']=df["first_name"]+ ' ' + df["last_name"]
    print(df)
    df.to_excel('Utilizatori.xlsx')
    print(df.describe())
    print( df["number_of_login"].mean())
    print(df["number_of_login"].std())



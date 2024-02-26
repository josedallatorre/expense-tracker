#import bot as bot
from datetime import datetime
import db
import csv_reader
import numpy as np
from psycopg2.extensions import register_adapter, AsIs
register_adapter(np.int64, AsIs)
print("hello world")

months = ['Gennaio','Febbraio','Marzo','Aprile','Maggio','Giugno','Luglio','Agosto', 'Settembre','Ottobre','Novembre','Dicembre']
for month in months:
    print(month)
    df = csv_reader.open_csv(month=month)
    df_cleaned = csv_reader.clean_df(df)
    n_rows = df_cleaned.__len__()
    for row in range(n_rows):
        t = csv_reader.row(df_cleaned,row)
        data= t[0]
        date_object = datetime.strptime(data, '%d/%m/%Y').date()
        a = t[1].item()
        descr = t[2]
        user_id = 1
        print(type(date_object))
        print(date_object)  # printed in default format
        print(a, type(a))
        t1 = (date_object.isoformat(), a, descr, user_id)
        cur, conn = db.connect()
        db.insert(cur, conn, t1)
        db.close(cur, conn)
#bot.echo_all
#db.connect



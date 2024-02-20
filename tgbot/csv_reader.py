import csv
import pandas
months = ['Gennaio','Febbraio','Marzo','Aprile','Maggio','Giugno','Luglio','Agosto','Settembre', 'Ottobre']
for month in months:
    with open('Bilancino - '+month+'.csv', newline='') as csvfile:
        df = pandas.read_csv(csvfile)
        df = df.rename(columns={' Ammontare': 'Ammontare'})
        df['Ammontare'] = df['Ammontare'].replace({'\€': ''}, regex=True)
        df.loc["Total", " Ammontare"] = df.Ammontare.sum()
        print(df)
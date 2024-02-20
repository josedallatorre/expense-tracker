import csv
import pandas
months = ['Gennaio','Febbraio','Marzo','Aprile','Maggio','Giugno','Luglio','Agosto','Settembre', 'Ottobre']
for month in months:
    with open('Bilancino - '+month+'.csv', newline='') as csvfile:
        df = pandas.read_csv(csvfile)
        print(df)
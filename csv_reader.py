import csv
months = ['Gennaio','Febbraio','Marzo','Aprile','Maggio','Giugno','Luglio','Agosto','Settembre']
tot: float = 0
for month in months:
    with open('Bilancino - '+month+'.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tot = tot + float(row[' Ammontare'].replace(",",".").replace("€","").replace(" ",""))
            print(row['Data'], row[' Ammontare'], row['Descrizione'])
print("Tot: "+str(tot))

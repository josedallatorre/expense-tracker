import csv

with open('new_file.csv', 'w', newline='') as csvfile:
    fieldnames = ['Data', ' Ammontare', 'Descrizione']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({fieldnames[0]: '10/10/10', fieldnames[1]: '€ -1,40', fieldnames[2]:"prova"})
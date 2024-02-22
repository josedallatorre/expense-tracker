import pandas
months = ['Gennaio','Febbraio','Marzo','Aprile','Maggio','Giugno','Luglio','Agosto']
for month in months:
    with open('Bilancino - '+month+'.csv', newline='') as csvfile:
        df = pandas.read_csv(csvfile)
        df.drop(df.columns[[0]], axis=1, inplace=True)
        df = df.rename(columns={' Ammontare': 'Ammontare'})
        df['Ammontare'] = df['Ammontare'].replace({'\€': ''}, regex=True)
        df['Ammontare'] = df['Ammontare'].apply(lambda x: x.replace('  ', ''))
        df['Ammontare'] = df['Ammontare'].apply(lambda x: x.replace(' ', ''))
        df['Ammontare'] = df['Ammontare'].apply(lambda x: x.replace(',', '.'))
        df['Ammontare'] = df['Ammontare'].apply(lambda x: x.replace('.', ''))
        #df[['AmmontareInt', 'AmmontareCent']] = df['Ammontare'].str.split('.', n=1, expand=True)
        df['Ammontare'] = df['Ammontare'].astype(int)
        #df['AmmontareInt'] = df['AmmontareInt'].astype(int)
        #df['AmmontareCent'] = df['AmmontareCent'].astype(int)
        df['Descrizione'] = df['Descrizione'].astype(str).str.cat(df['Unnamed: 4'].fillna('').astype(str), sep=' _ ').str.cat(df['Unnamed: 5'].fillna('').astype(str), sep=' _ ')
        df.drop(df.columns[[4]], axis=1, inplace=True)
        df.drop(df.columns[[3]], axis=1, inplace=True)

        print(df.dtypes)
        """
        TotalInt = df.AmmontareInt.sum()
        TotalCent = df.AmmontareCent.sum()
        """
        Total = df.Ammontare.sum()
        #print(df, "TotaleInt: " + str(TotalInt), "TotalCent: " +str(TotalCent), "Total: " +str(Total))
        print(df,"\n"+ str(Total))
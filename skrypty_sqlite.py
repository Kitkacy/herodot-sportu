import sqlite3
import csv
def dbcreater():
    sqliteConnection =sqlite3.connect("bazasqliteWiM.db")
    c = sqliteConnection.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS Zawodnicy(
    key INT AUTO_INCREMENT PRIMARY KEY,
    Imie VARCHAR(15),
    Nazwisko VARCHAR(15),
    Pseudonil VARCHAR(15),
    Plec BOOL,
    Narodowsc VARCHAR(15));""")
    c.execute("""CREATE TABLE IF NOT EXISTS Kategorie(
    key INT AUTO_INCREMENT PRIMARY KEY,
    NazwaKategorii VARCHAR(15),
    NumerZawodnika VARCHAR(15),
    LiczbaZlotychMedali INT,
    LiczbaSrebnychMedali INT,
    LiczbaBrazowychMedali INT,
    CzyAktynwy BOOL,
    DataEmerytura DATE,
    DataStart DATE);""")
    c.close(); 
    sqliteConnection.commit()
    sqliteConnection.close()
def READERzawodnicyfromCSV():
    with open('dataZaw.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            print(', '.join(row))
def READERkategoriefromCSV():
    with open('dataZ.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            print(', '.join(row))

def DodajZawodnika(g,im,na,ps,plec,nar):
    sqliteConnection =sqlite3.connect("bazasqliteWiM.db")
    c = sqliteConnection.cursor()
    c.execute("INSERT INTO Zawodnicy (key,Imie, Nazwisko,Pseudonil,Plec,Narodowsc) VALUES('"+g+"','"+str(im)+"','"+str(na)+"','"+str(ps)+"','"+str(plec)+"','"+str(nar)+"');")
    sqliteConnection.commit()
    c.close(); 
    sqliteConnection.commit()
    sqliteConnection.close()
def ZmienZawodnika(g,im,na,ps,plec,nar):
    sqliteConnection =sqlite3.connect("bazasqliteWiM.db")
    c = sqliteConnection.cursor()
   
    c.execute("UPDATE Zawodnicy SET key='"+str(g)+"',Imie='"+str(im)+"',Nazwisko='"+str(na)+"',Pseudonil='"+str(ps)+"',Plec='"+str(plec)+"',Narodowsc='"+str(nar)+ "' WHERE key ="+str(g))
    sqliteConnection.commit()
    c.close(); 
    sqliteConnection.commit()
    sqliteConnection.close()
def UsunZawodnika(g):
    sqliteConnection =sqlite3.connect("bazasqliteWiM.db")
    c = sqliteConnection.cursor()
    c.execute("DELETE FROM Zawodnicy WHERE key="+str(g))
    sqliteConnection.commit()
    c.close(); 
    sqliteConnection.commit()
    sqliteConnection.close()
def DodajKategorie(g,Ka,Nz,Lz,Ls,Lb,Za,De,DPz):
    sqliteConnection =sqlite3.connect("bazasqliteWiM.db")
    c = sqliteConnection.cursor()
    c.execute("INSERT INTO Kategorie (key,NazwaKategorii, NumerZawodnika,LiczbaZlotychMedali,LiczbaSrebnychMedali,LiczbaBrazowychMedali,CzyAktynwy,DataEmerytura,DataStart) VALUES('"+g+"','"+str(Ka)+"','"+str(Nz)+"','"+str(Lz)+"','"+str(Ls)+"','"+str(Lb)+"','"+str(Za)+"','"+str(De)+"','"+str(DPz)+"');")
    sqliteConnection.commit()
    c.close(); 
    sqliteConnection.commit()
    sqliteConnection.close()
def ZmienKategorie(g,Ka,Nz,Lz,Ls,Lb,Za,De,DPz):
    sqliteConnection =sqlite3.connect("bazasqliteWiM.db")
    c = sqliteConnection.cursor()
    c.execute("UPDATE Kategorie SET key='"+str(g)+"',NazwaKategorii='"+str(Ka)+"',NumerZawodnika='"+str(Nz)+"',LiczbaZlotychMedali='"+str(Lz)+"',LiczbaSrebnychMedali='"+str(Ls)+"',LiczbaBrazowychMedali='"+str(Lb)+"',CzyAktynwy='"+str(Za)+"',DataEmerytura='"+str(De)+"',DataStart='"+str(DPz)+ "' WHERE key ="+str(g))
    sqliteConnection.commit()
    c.close(); 
    sqliteConnection.commit()
    sqliteConnection.close()
def UsunKategorie(g):
    sqliteConnection =sqlite3.connect("bazasqliteWiM.db")
    c = sqliteConnection.cursor()
    c.execute("DELETE FROM Kategorie WHERE key="+str(g))
    sqliteConnection.commit()
    c.close(); 
    sqliteConnection.commit()
    sqliteConnection.close()
    
def ZRZUTZAW():
    with open('dataZaw.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([ 'NazwaKat','NumerZawodnika','LiczbaZ', 'LiczbaS','LiczbaB', 'CZYAKTYWNY','DATAEME', 'DATASTART',])
        writer.writerow([Ka, Nz,Lz,Ls,Lb,Za,De,DPz])
        print("ZAPISANO ZAWODNIKOW")
def ZRZUTKAT():
    with open('dataZaw.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([ 'Imie','Nazwisko','Pseudnoil', 'Plec','narodowsc'])
        writer.writerow([im,na,ps,plec,nar])
        print("ZAPISANO KATEGORIE")
def ZRZUTALL():
    with open('dataZ.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([ 'NazwaKat','NumerZawodnika','LiczbaZ', 'LiczbaS','LiczbaB', 'CZYAKTYWNY','DATAEME', 'DATASTART',])
        writer.writerow([Ka, Nz,Lz,Ls,Lb,Za,De,DPz])
        print("ZAPISANO ZAWODNIKOW")
    with open('dataZaw.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([ 'Imie','Nazwisko','Pseudnoil', 'Plec','narodowsc'])
        writer.writerow([im,na,ps,plec,nar])
        print("ZAPISANO KATEGORIE")
def dbclean():
    sqliteConnection =sqlite3.connect("bazasqliteWiM.db")
    c = sqliteConnection.cursor()
    c.execute("DROP TABLE Zawodnicy")
    c.execute("DROP TABLE Kategorie")
    c.execute("""CREATE TABLE IF NOT EXISTS Zawodnicy(
key INT AUTO_INCREMENT PRIMARY KEY,
Imie VARCHAR(15),
Nazwisko VARCHAR(15),
Pseudonil VARCHAR(15),
Plec BOOL,
Narodowsc VARCHAR(15));""")
    c.execute("""CREATE TABLE IF NOT EXISTS Kategorie(
key INT AUTO_INCREMENT PRIMARY KEY,
NazwaKategorii VARCHAR(15),
NumerZawodnika VARCHAR(15),
LiczbaZlotychMedali INT,
LiczbaSrebnychMedali INT,
LiczbaBrazowychMedali INT,
CzyAktynwy BOOL,
DataEmerytura DATE,
DataStart DATE);""")
    c.close(); 
    sqliteConnection.commit()
    sqliteConnection.close()
def GenerujDanePierwszaTablica():
    
    # Imie
    imie = random.choices(['Kacper', 'Amelia', 'Antoni', 'Zuzanna', 'Filip', 'Julia', 'Aleksander', 'Lena', 'Wojciech', 'Natalia', 'Adam', 'Ewa', 'Michał', 'Oliwia', 'Piotr', 'Karolina', 'Bartosz', 'Magdalena', 'Tomasz', 'Katarzyna'], k=1)
    
    # Nazwisko
    nazwisko = random.choices(['Nowak', 'Kowalski', 'Wiśniewski', 'Wójcik', 'Kowalczyk', 'Kamiński', 'Lewandowski', 'Zieliński', 'Szymański', 'Woźniak'], k=1)
    
    # Pseudonim
    pseudonim = random.choices(['Wiesmac', 'maly_bolo', 'walbrzych_KING', 'Ronald_Mcdonald', 'Twoja_stara', 'soltysica', 'lomza', 'gornik', 'wegiel_gang', 'krol_julian'], k=1)
    
    # Plec
    plec = random.choice(['1','0'])

    #Narodowosc
    narodowosc = random.choices(['Polska', 'Niemcy', 'Rosja', 'USA', 'Chiny', 'Japonia', 'Brazylia', 'Australia', 'Kanada', 'Indie','Sobiecin'], k=1)
    
    return [imie, nazwisko, pseudonim, plec, narodowosc]


#imie nazwisko pseudonim plec narodowosc 
#nazwa kategori zawodnik liczba zlotych medali liczba srebrnych medali liczba brazowych medali czy aktywny sprotowo data przejscia na emeryture data pierwszych zawodów


def GenerujDaneDrugaTablica(int i):
    
    # Nazwa kategori
    kategoria = random.choices(['Kolarstwo', 'Plywanie', 'Bieganie', 'Skok w dal', 'Skok wzwyż', 'Skok o tyczce', 'Rzut oszczepem', 'Rzut mlotem', 'Rzut dyskiem', 'Rzut kulą'], k=1)
    
    # Zawodnik
    
    zawodnik = random.randiant(0,i)
    
    # Liczba zlotych medali
    zloty = random.choices(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], k=1)
    
    # Liczba srebrnych medali
    srebrny = random.choices(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], k=1)
    
    # Liczba brazowych medali
    brazowy = random.choices(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], k=1)
    
    # Czy aktywny sportowo
    random_bool = random.choice(['1','0'])
    
    # Data przejscia na emeryture
    if(random_bool)
        data_emerytury = random.choices(['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999','2012'], k=1)
    else:
        data_emerytury=''
    # Data pierwszych zawodów
    data_zawodow = random.choices(['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997','2000'], k=1)
    
    return [kategoria, zawodnik, zloty, srebrny, brazowy, random_bool, data_emerytury, data_zawodow]

def dblosowe():
    qliteConnection =sqlite3.connect("bazasqliteWiM.db")
    c = sqliteConnection.cursor()
    dok=c.execute("SELECT COUNT(*) FROM Zawodnicy")
    for i in dok:
        h=str(i)
        g=h[1:-2]
        break
    a=GenerujDanePierwszaTablica()
        #dok=int(dok)
        #print("///////////")
        #print(dok.type)
        #print(dok)
    print("ILE SPORTOWCOW WYGENEROWAC")
    x=input()
    for i in range(int(x)):
        g=int(g)
        g=g+1
        g=str(g)
        a=GenerujDanePierwszaTablica()
        print(a)
        c.execute("INSERT INTO Zawodnicy (key,Imie, Nazwisko,Pseudonil,Plec,Narodowsc) VALUES('"+g+"','"+str(*a[0])+"','"+str(*a[1])+"','"+str(*a[2])+"','"+str(*a[3])+"','"+str(*a[4])+"');")
        sqliteConnection.commit()
        print("ILE SPORTOWCOW Kategorii")
        x=input()
        for i in range(int(x)):
            g=int(g)
            g=g+1
            g=str(g)
            a=GenerujDaneDrugaTablica(g)
            print(a)
            dok=c.execute("SELECT COUNT(*) FROM Kategorie")
            for i in dok:
                h=str(i)
                g2=h[1:-2]
                break
            #return [kategoria, zawodnik, zloty, srebrny, brazowy, random_bool, data_emerytury, data_zawodow]
            #print("INSERT INTO Zawodnicy (key,Imie, Nazwisko,Pseudonil,Plec,Narodowsc) VALUES('"+g+"','"+str(*a[0])+"','"+str(*a[1])+"','"+str(*a[2])+"','"+str(*a[3])+"','"+str(*a[4])+str(*a[5])+"','"+str(*a[6])+"','"+str(*a[7])+"');")
            c.execute("INSERT INTO Kategorie (key,NazwaKategorii, NumerZawodnika,LiczbaZlotychMedali,LiczbaSrebnychMedali,LiczbaBrazowychMedali,CzyAktynwy,DataEmerytura,DataStart) VALUES('"+g2+"','"+str(*a[0])+"','"+str(*a[1])+"','"+str(*a[2])+"','"+str(*a[3])+"','"+str(*a[4])+"','"+str(*a[5])+"','"+str(*a[6])+"','"+str(*a[7])+"');")
            sqliteConnection.commit()
    c.close(); 
    sqliteConnection.commit()
    sqliteConnection.close()
    
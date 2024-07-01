import csv
import sqlite3
import random
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
    narodowosc = random.choices(['Polska', 'Niemcy', 'Rosja', 'USA', 'Chiny', 'Japonia', 'Brazylia', 'Australia', 'Kanada', 'Indie'], k=1)
    
    return [imie, nazwisko, pseudonim, plec, narodowosc]


#imie nazwisko pseudonim plec narodowosc 
#nazwa kategori zawodnik liczba zlotych medali liczba srebrnych medali liczba brazowych medali czy aktywny sprotowo data przejscia na emeryture data pierwszych zawodów


def GenerujDaneDrugaTablica( i):
    
    # Nazwa kategori
    kategoria = random.choices(['Kolarstwo', 'Plywanie', 'Bieganie', 'Skok w dal', 'Skok wzwyż', 'Skok o tyczce', 'Rzut oszczepem', 'Rzut mlotem', 'Rzut dyskiem', 'Rzut kulą','wyciskanie ciężarów','szachy','szermierka'], k=1)
    
    # Zawodnik
    
    zawodnik = random.randint(0,int(i))
    zawodnik=str(zawodnik)
    zawodnik=list(zawodnik.split("-"))
    
    # Liczba zlotych medali
    zloty = random.choices(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], k=1)
    
    # Liczba srebrnych medali
    srebrny = random.choices(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], k=1)
    
    # Liczba brazowych medali
    brazowy = random.choices(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], k=1)
    
    # Czy aktywny sportowo
    random_bool = random.choice(['1','0'])
    
    # Data przejscia na emeryture
    if(random_bool=='1'):
        data_emerytury = random.choices(['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010','2012'], k=1)
        dzien=random.choices(['01','02','03','05','07','10','12','14','18','19','20','21','22','26','27','09','13','08','24'])
        miesiac=random.choices(['01','02','03','04','05','06','07','08','09','10','11','12'])
        data_emerytury[0]=data_emerytury[0]+'-'+miesiac[0]+'-'+dzien[0]
    else:
        data_emerytury=['2222-10-31']
    # Data pierwszych zawodów
    data_zawodow = random.choices(['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997','2000'], k=1)
    dzien=random.choices(['01','02','03','05','07','10','12','14','18','19','20','21','22','26','27','09','13','08','24'])
    miesiac=random.choices(['01','02','03','04','05','06','07','08','09','10','11','12'])
    data_zawodow[0]=data_zawodow[0]+'-'+miesiac[0]+'-'+dzien[0]
    return [kategoria, zawodnik, zloty, srebrny, brazowy, random_bool, data_emerytury, data_zawodow]


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
NumerZawodnika INT,
LiczbaZlotychMedali INT,
LiczbaSrebnychMedali INT,
LiczbaBrazowychMedali INT,
CzyAktynwy BOOL,
DataEmerytura DATE,
DataStart DATE);""")


print("(1)WPROWADZIĆ CZY (2)ZRZUT DANYCH")
x = input()
print(x)
if(x=='1'):
    print("wprowadzic (1)ZAWODNICY CZY (2)KATEGOIRE  -- (3)LOSOWE DANE")
    y=input()
    if(y=='1'):
        dok=c.execute("SELECT COUNT(*) FROM Zawodnicy")
        for i in dok:
            #print(i)
            h=str(i)
            g=h[1:-2]
            #print(g)
            break
        w='T'
        while(w=='T'):
            im = input("Podaj imie")
            na = input("Podaj nazwisko")
            ps = input("podaj pseudonil (Opcionalne)")
            plec=input("Plec (Mezcyzna = 1) (Kobieta=0)")
            nar=input("Podaj narodowosc")
            print("WPROWADZONE DANE:")
            print(im)
            print(na)
            print(ps)
            print(plec)
            print(nar)
            print("CZY POWTORZYĆ? (T)")
            w=input() 
        g=int(g)
        g=g+1
        g=str(g)

        c.execute("INSERT INTO Zawodnicy (key,Imie, Nazwisko,Pseudonil,Plec,Narodowsc) VALUES('"+g+"','"+str(im)+"','"+str(na)+"','"+str(ps)+"','"+str(plec)+"','"+str(nar)+"');")
        sqliteConnection.commit()    
      
            
    elif(y=='3'):
        dok=c.execute("SELECT COUNT(*) FROM Zawodnicy")
        for i in dok:
            #print(i)
            h=str(i)
            g=h[1:-2]
            print(g)
            break
        a=GenerujDanePierwszaTablica()
        print("ILE SPORTOWCOW WYGENEROWAC")
        x=input()
        for i in range(int(x)):
            g=int(g)
            g=g+1
            g=str(g)
            a=GenerujDanePierwszaTablica()
            #print(a)
            c.execute("INSERT INTO Zawodnicy (key,Imie, Nazwisko,Pseudonil,Plec,Narodowsc) VALUES('"+g+"','"+str(*a[0])+"','"+str(*a[1])+"','"+str(*a[2])+"','"+str(*a[3])+"','"+str(*a[4])+"');")
        sqliteConnection.commit()
        print("ILE SPORTOWCOW Kategorii")
        dok=c.execute("SELECT COUNT(*) FROM Kategorie")
        for i in dok:
            #print(i)
            h=str(i)
            g=h[1:-2]
            print(g)
            break
        x=input()
        for i in range(int(x)):
            g=int(g)
            g=g+1
            g=str(g)
            a=GenerujDaneDrugaTablica(g)
           
            c.execute("INSERT INTO Kategorie (key,NazwaKategorii, NumerZawodnika,LiczbaZlotychMedali,LiczbaSrebnychMedali,LiczbaBrazowychMedali,CzyAktynwy,DataEmerytura,DataStart) VALUES('"+g+"','"+str(*a[0])+"','"+str(*a[1])+"','"+str(*a[2])+"','"+str(*a[3])+"','"+str(*a[4])+"','"+str(*a[5])+"','"+str(*a[6])+"','"+str(*a[7])+"');")
            sqliteConnection.commit()
            
    elif(y=='2'):
        w='T'
        dok=c.execute("SELECT COUNT(*) FROM Kategorie")
        for i in dok:
            h=str(i)
            g=h[1:-2]
            #g=g+1
            break
        #print(dok2)
        while(w=='T'):
            Ka = input("Nazwa KAtegorii")
            Nz = input("Numer Zawodnika")
            Lz = input("Liczba zlotych medali")
            Ls=input("Liczba srebnych medali")
            Lb=input("Liczba brazowych medali")
            Za = input("Czy zawodnik aktywny sportowo")
            De=input("Data Przejscia na Emeryture YYYY-MM-DD (Opcionalne)")
            if De=='':
                De="2222-10-31"
            DPz=input("Data Pierwszych zawodow YYYY-MM-DD")
            print("CZY POWTORZYĆ? (T)")
            w=input()
        
        print(g)
        g=int(g)
        g=g+1
        g=str(g)
        print(g)
        
        c.execute("INSERT INTO Kategorie (key,NazwaKategorii, NumerZawodnika,LiczbaZlotychMedali,LiczbaSrebnychMedali,LiczbaBrazowychMedali,CzyAktynwy,DataEmerytura,DataStart) VALUES('"+str(g)+"','"+str(Ka)+"','"+str(Nz)+"','"+str(Lz)+"','"+str(Ls)+"','"+str(Lb)+"','"+str(Za)+"','"+str(De)+"','"+str(DPz)+"');")
        sqliteConnection.commit()
 
            
else:
    dok=c.execute("SELECT * FROM Kategorie")
    with open('dataZ.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['key','NazwaKat','NumerZawodnika','LiczbaZ', 'LiczbaS','LiczbaB', 'CZYAKTYWNY','DATAEME', 'DATASTART'])
        for d in dok:
            writer.writerow([d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8]])
        print("ZAPISANO KATEGORIE")
    dok=c.execute("SELECT * FROM Zawodnicy")
    with open('dataZaw.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([ 'lp','Imie','Nazwisko','Pseudnoil', 'Plec','narodowsc'])
        for d in dok:
            writer.writerow([d[0],d[1],d[2],d[3],d[4],d[5]])
    print("ZAPISANO ZAWODNIKOW")
    
c.close(); 
sqliteConnection.commit()
sqliteConnection.close()
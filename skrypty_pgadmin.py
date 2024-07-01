import csv
import psycopg
import simplejson

def DBcreate(plikJSON):
    with open(plikJSON) as db_con_file:
        creds = simplejson.loads(db_con_file.read())
    con = psycopg.connect(
             host=creds['host_name'],
             user=creds['user_name'],
             dbname=creds['db_name'],
             password=creds['password'],
             port=creds['port_number'])
    c=con.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS Zawodnicy(
    key INT PRIMARY KEY,
    Imie VARCHAR(15),
    Nazwisko VARCHAR(15),
    Pseudonil VARCHAR(15),
    Plec BOOL,
    Narodowsc VARCHAR(15));""")
    c.execute("""CREATE TABLE IF NOT EXISTS Kategorie(
    key INT PRIMARY KEY,
    NazwaKategorii VARCHAR(30),
    NumerZawodnika VARCHAR(15),
    LiczbaZlotychMedali INT,
    LiczbaSrebnychMedali INT,
    LiczbaBrazowychMedali INT,
    CzyAktynwy BOOL,
    DataEmerytura DATE,
    DataStart DATE);""")
    con.commit()
    c.close()
    con.close()
    print("k")

def CSVtoDB (dataZ, dataZaw, plikJSON):
    print("rozpoczęto przerzut informacji")
    with open(plikJSON) as db_con_file:
        creds = simplejson.loads(db_con_file.read())
    con = psycopg.connect(
             host=creds['host_name'],
             user=creds['user_name'],
             dbname=creds['db_name'],
             password=creds['password'],
             port=creds['port_number'])
    c=con.cursor()
    with open(dataZ,"r") as f:
        reader = csv.reader(f)
        i = 0
        for row in reader:
            if i == 0:
                i=i+1
                continue
            print(row)
            c.execute('''INSERT INTO Kategorie (key,NazwaKategorii , NumerZawodnika, LiczbaZlotychMedali, LiczbaSrebnychMedali, LiczbaBrazowychMedali,CzyAktynwy,DataEmerytura,DataStart) 
                      VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);''', (row))
    with open(dataZaw,"r") as f:
        reader = csv.reader(f)
        i = 0
        for row in reader:
            if i == 0:
                i=i+1
                continue
            print(row)
            c.execute('''INSERT INTO Zawodnicy (key,Imie, Nazwisko, Pseudonil, Plec,Narodowsc) 
                      VALUES (%s,%s,%s,%s,%s,%s);''', (row))
    con.commit()
    c.close()
    con.close()
    print("zakonczono dane przerzucone")

def addZawodnicy (plikJSON,g,im,na,ps,plec,nar):
    with open(plikJSON) as db_con_file:
        creds = simplejson.loads(db_con_file.read())
    con = psycopg.connect(
             host=creds['host_name'],
             user=creds['user_name'],
             dbname=creds['db_name'],
             password=creds['password'],
             port=creds['port_number'])
    c=con.cursor()
    c.execute("INSERT INTO Zawodnicy (key,Imie, Nazwisko,Pseudonil,Plec,Narodowsc) VALUES('"+g+"','"+str(im)+"','"+str(na)+"','"+str(ps)+"','"+str(plec)+"','"+str(nar)+"');")
    con.commit()
    c.close()
    con.close
def updateZawodnicy (plikJSON,g,im,na,ps,plec,nar):
    with open(plikJSON) as db_con_file:
        creds = simplejson.loads(db_con_file.read())
    con = psycopg.connect(
             host=creds['host_name'],
             user=creds['user_name'],
             dbname=creds['db_name'],
             password=creds['password'],
             port=creds['port_number'])
    c=con.cursor()
    c.execute("UPDATE Zawodnicy SET key='"+str(g)+"',Imie='"+str(im)+"',Nazwisko='"+str(na)+"',Pseudonil='"+str(ps)+"',Plec='"+str(plec)+"',Narodowsc='"+str(nar)+ "' WHERE key ="+str(g))
    con.commit()
    c.close()
    con.close
def deleteZawodnicy (plikJSON,g):
    with open(plikJSON) as db_con_file:
        creds = simplejson.loads(db_con_file.read())
    con = psycopg.connect(
             host=creds['host_name'],
             user=creds['user_name'],
             dbname=creds['db_name'],
             password=creds['password'],
             port=creds['port_number'])
    c=con.cursor()
    c.execute("DELETE FROM Zawodnicy WHERE key="+str(g))
    con.commit()
    c.close()
    con.close
def addKategorie (plikJSON,g,Ka,Nz,Lz,Ls,Lb,Za,De,DPz):
    with open("database_creds.json") as db_con_file:
        creds = simplejson.loads(db_con_file.read())
    con = psycopg.connect(
             host=creds['host_name'],
             user=creds['user_name'],
             dbname=creds['db_name'],
             password=creds['password'],
             port=creds['port_number'])
    c=con.cursor()
    c.execute("INSERT INTO Kategorie (key,NazwaKategorii, NumerZawodnika,LiczbaZlotychMedali,LiczbaSrebnychMedali,LiczbaBrazowychMedali,CzyAktynwy,DataEmerytura,DataStart) VALUES('"+g+"','"+str(Ka)+"','"+str(Nz)+"','"+str(Lz)+"','"+str(Ls)+"','"+str(Lb)+"','"+str(Za)+"','"+str(De)+"','"+str(DPz)+"');")
    con.commit()
    c.close()
    con.close()
def updateKategorie (plikJSON,g,Ka,Nz,Lz,Ls,Lb,Za,De,DPz):
    with open("database_creds.json") as db_con_file:
        creds = simplejson.loads(db_con_file.read())
    con = psycopg.connect(
             host=creds['host_name'],
             user=creds['user_name'],
             dbname=creds['db_name'],
             password=creds['password'],
             port=creds['port_number'])
    c=con.cursor()
    c.execute("UPDATE Kategorie SET key='"+str(g)+"',NazwaKategorii='"+str(Ka)+"',NumerZawodnika='"+str(Nz)+"',LiczbaZlotychMedali='"+str(Lz)+"',LiczbaSrebnychMedali='"+str(Ls)+"',LiczbaBrazowychMedali='"+str(Lb)+"',CzyAktynwy='"+str(Za)+"',DataEmerytura='"+str(De)+"',DataStart='"+str(DPz)+ "' WHERE key ="+str(g))
    con.commit()
    c.close()
    con.close()
def deleteKategorie (plikJSON,g):
    with open("database_creds.json") as db_con_file:
        creds = simplejson.loads(db_con_file.read())
    con = psycopg.connect(
             host=creds['host_name'],
             user=creds['user_name'],
             dbname=creds['db_name'],
             password=creds['password'],
             port=creds['port_number'])
    c=con.cursor()
    c.execute("DELETE FROM Kategorie WHERE key="+str(g))
    con.commit()
    c.close()
    con.close()
def CleanDB(plikJSON):
    with open(plikJSON) as db_con_file:
        creds = simplejson.loads(db_con_file.read())
    con = psycopg.connect(
             host=creds['host_name'],
             user=creds['user_name'],
             dbname=creds['db_name'],
             password=creds['password'],
             port=creds['port_number'])
    c=con.cursor()
    c.execute("""DROP TABLE Zawodnicy""")
    c.execute("""DROP TABLE Kategorie""")
    c.execute("""CREATE TABLE IF NOT EXISTS Zawodnicy(
    key INT PRIMARY KEY,
    Imie VARCHAR(15),
    Nazwisko VARCHAR(15),
    Pseudonil VARCHAR(15),
    Plec BOOL,
    Narodowsc VARCHAR(15));""")
    c.execute("""CREATE TABLE IF NOT EXISTS Kategorie(
    key INT PRIMARY KEY,
    NazwaKategorii VARCHAR(30),
    NumerZawodnika VARCHAR(15),
    LiczbaZlotychMedali INT,
    LiczbaSrebnychMedali INT,
    LiczbaBrazowychMedali INT,
    CzyAktynwy BOOL,
    DataEmerytura DATE,
    DataStart DATE);""")
    con.commit()
    c.close()
    con.close()
#with open ("database_creds.json") as f:
#    db_creds = simplejson.load(f)
#    DBcreate(db_creds)
#    CSVtoDB("Books.csv","Clients.csv",db_creds)
def SelectAll (connection: psycopg.connection, tableName):
    cursor = connection.cursor()
    selected = cursor.execute(f"SELECT * FROM {tableName}").fetchall()
    cursor.close()
    return selected

def Select (connection: psycopg.connection, tableName, selectionType, selection):
    cursor = connection.cursor()
    selected = cursor.execute(f"SELECT * FROM {tableName} WHERE {selectionType} = '{selection}'").fetchall()
    cursor.close()
    return selected 

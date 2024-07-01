import csv
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np

sqliteConnection =sqlite3.connect("bazasqliteWiM.db")
c = sqliteConnection.cursor()


print("(1)Pojedynczy sportowcy CZY (2)narodowości")
x = input()
if(x=='1'):
    print("Podaj numer zawodnika")
    y=input()
    dok=c.execute("SELECT * FROM Zawodnicy WHERE key="+str(y))
    for d in dok:
        print(d)
        imie=d[1]
        nazwisko=d[2]
        ksywa=d[3]
    zloto=0
    srebro=0
    braz=0
    dok2=c.execute("SELECT * FROM Kategorie WHERE NumerZawodnika="+str(y))
    for d2 in dok2:
        zloto+=int(d2[3])
        srebro+=int(d2[4])
        braz+=int(d2[5])
    medals = ['Złoto', 'Srebro', 'Brąz']
    values = [zloto, srebro, braz]
    plt.bar(medals, values, color=['gold', 'silver', 'brown'])
    plt.title(f'{imie} ({ksywa}) {nazwisko}')
    plt.ylabel('Ilość medali')
    ax = plt.gca()
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    plt.show()
else:
    #SELECT tablename1.colunmnname, tablename2.columnname FROM tablename1 JOIN tablename2
    #LEFT JOIN table_nameB ON table_nameA.column_name = table_nameB.column_name;
    dok=c.execute("UPDATE Zawodnicy SET Narodowsc='Polska' WHERE Narodowsc='Polak' ")
    dok=c.execute("SELECT Zawodnicy.Narodowsc,Kategorie.LiczbaZlotychMedali,Kategorie.LiczbaSrebnychMedali,Kategorie.LiczbaBrazowychMedali FROM Zawodnicy LEFT JOIN Kategorie ON Zawodnicy.key = Kategorie.NumerZawodnika")
    narodowosci=[]
    zlote=[]
    srebne=[]
    brazowe=[]
    for d in dok:
        #print(d)
        d=[0 if v is None else v for v in d]
        if d[0] in narodowosci:
            indexx = narodowosci.index(d[0])
            if d[1] is None:
                pass
            else:
                zlote[indexx]+=int(d[1])
            if d[2] is None:
                pass
            else:
                srebne[indexx]+=int(d[2])
            if d[3] is None:
                pass
            else:    
                brazowe[indexx]+=int(d[3])
        else:
            narodowosci.append(d[0])
            zlote.append(d[1])
            srebne.append(d[2])
            brazowe.append(d[3])
    print(narodowosci)
    print(zlote)
    print(srebne)
    print(brazowe)
    #Le wykres
    N = len(narodowosci)

    ind = np.arange(N)
    #ind=0
    width = N/40

    fig = plt.figure()
    ax = fig.add_subplot(111)

    rects1 = ax.bar(ind, zlote, width, color='gold')
    rects2 = ax.bar(ind+width, srebne, width, color='silver')
    rects3 = ax.bar(ind+width*2, brazowe, width, color='brown')

    ax.set_ylabel('Ilość medali')
    ax.set_xticks(ind+width)
    ax.set_xticklabels(narodowosci)
    ax.legend((rects1[0], rects2[0], rects3[0]), ('Złoto', 'Srebro', 'Brąz'))
    ax = plt.gca()
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    plt.show()


    c.close(); 
    sqliteConnection.commit()
    sqliteConnection.close()
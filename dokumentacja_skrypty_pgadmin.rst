Dokumentacja skryptu pgadmin.py
====================================

Opis
-------

Ten skrypt jest przeznaczony do zarządzania bazami danych PostgreSQL, w szczególności do tworzenia tabel oraz importowania danych z plików CSV do tych tabel.


Funkcje
-------

- **def DBcreate(plikJSON)**
    Tworzy połączenie z bazą danych postgres i dwie tabele: Zawodnicy i Kategorie, jeśli nie istnieją. 
- **CCSVtoDB (dataZ, dataZaw, plikJSON)**
   Przeżuca dane z plików csv do bazy danych.
- **addZawodnicy (plikJSON,g,im,na,ps,plec,nar)**
    Dodaje nowego zawodnika do tabeli Zawodnicy.
- **updateZawodnicy (plikJSON,g,im,na,ps,plec,nar)**
    Aktualizuje dane zawodnika w tabeli Zawodnicy.
- **deleteZawodnicy (plikJSON,g)**
    Usuwa zawodnika z tabeli Zawodnicy na podstawie klucza podstawowego.
- **addKategorie (plikJSON,g,Ka,Nz,Lz,Ls,Lb,Za,De,DPz)**
    Funkcja służy do dodawania nowego rekordu do tabeli Kategorie. 
- **updateKategorie (plikJSON,g,Ka,Nz,Lz,Ls,Lb,Za,De,DPz)**
    Aktualizuje dane rekordu w tabeli Kategorie.
- **deleteKategorie (plikJSON,g)**
    Usuwa rekord z tabeli Zawodnicy na podstawie klucza podstawowego.
- **CleanDB(plikJSON)**
    Usawa tablice i zastępuje je nowymi.

Struktury Tabel
---------------

- **Zawodnicy**

  - `key`: INT PRIMARY KEY
  - `Imie`: VARCHAR(15)
  - `Nazwisko`: VARCHAR(15)
  - `Pseudonil`: VARCHAR(15)
  - `Plec`: BOOL
  - `Narodowsc`: VARCHAR(15)

- **Kategorie**

  - `key`: INT PRIMARY KEY
  - `NazwaKategorii`: VARCHAR(30)
  - `NumerZawodnika`: VARCHAR(15)
  - `LiczbaZlotychMedali`: INT
  - `LiczbaSrebnychMedali`: INT
  - `LiczbaBrazowychMedali`: INT
  - `CzyAktynwy`: BOOL
  - `DataEmerytura`: DATE
  - `DataStart`: DATE

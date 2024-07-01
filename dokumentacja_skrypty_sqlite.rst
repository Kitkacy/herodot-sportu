Dokumentacja skryptu sqlite.py
==================================

Opis
-------

Skrypty_sqlite.py to zbiór funkcji do zarządzania bazą danych SQLite, w tym tworzenia tabel, dodawania, aktualizowania i usuwania rekordów, oraz odczytywania danych z plików CSV.

Funkcje
---------

**dbcreater()**
    Tworzy połączenie z bazą danych SQLite bazasqliteWiM.db i dwie tabele: Zawodnicy i Kategorie, jeśli nie istnieją. 

**READERzawodnicyfromCSV()**
    Odczytuje dane z pliku CSV dataZaw.csv i wyświetla je w konsoli.

**READERkategoriefromCSV()**
    Odczytuje dane z pliku CSV dataZ.csv i wyświetla je w konsoli.

**DodajZawodnika(g, im, na, ps, plec, nar)**
    Dodaje nowego zawodnika do tabeli Zawodnicy.

**ZmienZawodnika(g, im, na, ps, plec, nar)**
    Aktualizuje dane zawodnika w tabeli Zawodnicy.

**UsunZawodnika(g)**
    Usuwa zawodnika z tabeli Zawodnicy na podstawie klucza podstawowego.

**DodajKategorie(g, Ka, Nz, Lz, Ls, Lb, Za, De, DPz)**
    Funkcja służy do dodawania nowego rekordu do tabeli Kategorie. 
     
**ZmienKategorie(g, Ka, Nz, Lz, Ls, Lb, Za, De, DPz)**
    Aktualizuje dane rekordu w tabeli Kategorie.
**UsunKategorie(g)**
    Usuwa rekord z tabeli Zawodnicy na podstawie klucza podstawowego.
**ZRZUTZAW()**
    Zapisuje/nadpisuje aktualny stan tabeli Zawodnicy do pliku csv.
**ZRZUTZKAT()**
    Zapisuje/nadpisuje aktualny stan tabeli Kategorie do pliku csv.
**ZRZUTZALL()**
    Zapisuje/nadpisuje aktualny stan obu tabel do pliku csv.
**dbclean()**
    Usawa tablice i zastępuje je nowymi.
**GenerujDanePierwszaTablica()**
    Generuje przykładowe dane do tablicy Zawodnicy.
**GenerujDaneDrugaTablica(int i)**
    Generuje przykładowe dane do tablicy Zawodnicy.
**dblosowe()**
    Korzysta z GenerujDaneDrugaTablica i GenerujDanePierwszaTablica do generowania wielu danych naraz.
    
Struktura tabel
----------------

Zawodnicy
    - key INT AUTO_INCREMENT PRIMARY KEY
    - Imie VARCHAR(15)
    - Nazwisko VARCHAR(15)
    - Pseudonil VARCHAR(15)
    - Plec BOOL
    - Narodowsc VARCHAR(15)

Kategorie
    - key INT AUTO_INCREMENT PRIMARY KEY
    - NazwaKategorii VARCHAR(15)
    - NumerZawodnika VARCHAR(15)
    - LiczbaZlotychMedali INT
    - LiczbaSrebnychMedali INT
    - LiczbaBrazowychMedali INT
    - CzyAktynwy BOOL
    - DataEmerytura DATE (Jeśli brak, zostaje ustawiona wartość 2222-10-31)
    - DataStart DATE

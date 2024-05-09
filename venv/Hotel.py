from abc import ABC, abstractmethod

class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar=ar

    @abstractmethod
    def info(self):
        pass

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar=10000):
        super().__init__(szobaszam, ar)

    def info(self):
        return f"Egyágyas szoba, Szobaszám: {self.szobaszam}, Ár: {self.ar} Ft"

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar=15000):
        super().__init__(szobaszam, ar)

    def info(self):
        return f"Kétagyas szoba, Szobaszám: {self.szobaszam}, Ár: {self.ar} Ft"

class Szalloda:
    def __init__(self, nev):
        self.nev=nev
        self.szobak=[]

    def szoba_hozzaad(self, szoba):
        self.szobak.append(szoba)

    def szoba_info(self):
        for szoba in self.szobak:
            print(szoba.info())

class Foglalas:
    def __init__(self):
        self.foglalasok=[]

    def foglal(self, szoba, nap):
        self.foglalasok.append((szoba, nap))

    def foglalasok_listaja(self):
        for szoba, nap in self.foglalasok:
            print(f"Foglalás: Szobaszám: {szoba.szobaszam}, Nap: {nap}")


class Foglalas:
    def __init__(self):
        self.foglalasok=[]
        self.kovetkezo_id=1

    def foglal(self, szoba, nap):
        for f in self.foglalasok:
            if f['szoba'].szobaszam==szoba.szobaszam and f['nap']==nap:
                print(f"Ez a szoba ({szoba.szobaszam}) ezen a napon ({nap}) már foglalt.")
                return None
        self.foglalasok.append({"id": self.kovetkezo_id, "szoba": szoba, "nap": nap})
        self.kovetkezo_id+=1
        print(f"Foglalás sikeres: {szoba.szobaszam} szobaszám, {nap} nap, {szoba.ar} Ft")
        return szoba.ar

    def foglalas_lemond(self, foglalas_id):
        for i, f in enumerate(self.foglalasok):
            if f['id']==foglalas_id:
                self.foglalasok.pop(i)
                print(f"Foglalás lemondva: ID {foglalas_id}")
                return True
        print("Nincs ilyen foglalás azonosító.")
        return False

    def foglalasok_listaja(self):
        if not self.foglalasok:
            print("Nincsenek foglalások.")
        for f in self.foglalasok:
            print(f"Foglalás ID: {f['id']}, Szobaszám: {f['szoba'].szobaszam}, Nap: {f['nap']}, Ár: {f['szoba'].ar} Ft")


import datetime


class Szalloda:
    def __init__(self, nev):
        self.nev=nev
        self.szobak = []

    def szoba_hozzaad(self, szoba):
        self.szobak.append(szoba)

    def szoba_info(self):
        for szoba in self.szobak:
            print(szoba.info())

    def get_szoba(self, szobaszam):
        for szoba in self.szobak:
            if szoba.szobaszam==szobaszam:
                return szoba
        return None


def main():
    szalloda = Szalloda("Best Hotel")
    szalloda.szoba_hozzaad(EgyagyasSzoba(101))
    szalloda.szoba_hozzaad(KetagyasSzoba(102))
    szalloda.szoba_hozzaad(EgyagyasSzoba(103))

    foglalas = Foglalas()

    while True:
        print("\nVálassz az alábbi opciók közül:")
        print("1: Foglalás")
        print("2: Foglalás lemondása")
        print("3: Foglalások listázása")
        print("4: Kilépés")
        valasz = input("Választás: ")

        if valasz=="1":
            szobaszam=int(input("Add meg a szobaszámot: "))
            datum=input("Add meg a foglalás dátumát (yyyy-mm-dd formátumban): ")
            datum_obj=datetime.datetime.strptime(datum, '%Y-%m-%d')
            if datum_obj.date()<=datetime.date.today():
                print("Hiba: A dátum nem lehet a mai napnál korábbi.")
            else:
                szoba=szalloda.get_szoba(szobaszam)
                if szoba:
                    foglalas.foglal(szoba, datum)
                else:
                    print("Nem létező szoba.")

        elif valasz=="2":
            foglalas_id=int(input("Add meg a foglalás azonosítóját: "))
            if not foglalas.foglalas_lemond(foglalas_id):
                print("Hiba: Nem létező foglalás azonosító.")

        elif valasz=="3":
            foglalas.foglalasok_listaja()

        elif valasz=="4":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás. Kérlek, próbáld újra.")


if __name__ == "__main__":
    main()
#e

import time
import sys
import random

def wyswietl_tekst_powoli(tekst, opoznienie=0.01):
    for litera in tekst:
        sys.stdout.write(litera)
        sys.stdout.flush()
        time.sleep(opoznienie)
    print()

def start():
    wyswietl_tekst_powoli("DROGA BEZ POWROTU")
    wyswietl_tekst_powoli("Na pytania tak lub nie odpowiadaj 'tak' lub 'nie'")
    wyswietl_tekst_powoli("Na pytania, gdzie jest więcej opcji, odpowiadaj literą, która jest przypisana do opcji.")
    wyswietl_tekst_powoli("Właśnie jedziesz samochodem przez las, dzwoni twój telefon, próbując po niego sięgnąć wrzucasz go na wycieraczkę.")
    wyswietl_tekst_powoli("Sięgasz po niego i przez nieuwagę zderzasz się ze samochodem stojącym na drodze.")
    wyswietl_tekst_powoli("Wysiadasz dowiadujesz się, że samochodem, w który wjechałeś, jechały 3 osoby i stoją na drodze, ponieważ najechali na drut kolczasty, który leżał na drodze, i poprzebijali opony.")
    wyswietl_tekst_powoli("Próbujesz odpalić swój samochód, lecz on nie reaguje.")
    wyswietl_tekst_powoli("Twoim zadaniem jest przeżyć, jak sobie poradzisz?")
    krok_pierwszy()

def krok_pierwszy():
    while True:
        wyswietl_tekst_powoli("Czy idziesz do lasu-l, idziesz wzdłuż drogi-d, czy zostajesz w samochodzie-s? ")
        wybor = input("> ").lower()
        if wybor == "l":
            do_lasu()
            break
        elif wybor == "d":
            wzdluz_drogi()
            break
        elif wybor == "s":
            zostajesz_w_samochodzie()
            break
        else:
            wyswietl_tekst_powoli("Nie rozumiem tego wyboru. Spróbuj ponownie.")

def do_lasu():
    wyswietl_tekst_powoli("Idziesz do lasu.")
    wyswietl_tekst_powoli("W lesie znajdujecie drewnianą chatę.")
    while True:
        wyswietl_tekst_powoli("Czy do niej wchodzicie? [tak/nie]")
        wybor = input("> ").lower()
        if wybor == "tak":
            chata()
            break
        elif wybor == "nie":
            wyswietl_tekst_powoli("Idziecie dalej w las.")
            wyswietl_tekst_powoli("Znajdujecie wraki samochodów.")
            wyswietl_tekst_powoli("Nagle podjerzdza samochód, który choluje wasze auto")
            wraki1()
            break
        else:
            wyswietl_tekst_powoli("Nie rozumiem tego wyboru. Spróbuj ponownie.")

def chata():
    wyswietl_tekst_powoli("W chacie znajdujecie dziwne przedmioty.")
    wyswietl_tekst_powoli("Znajdujecie również reżtki ciał.")
    while True:
        wyswietl_tekst_powoli("Przez okno zauważacie, że ktoś idzie do chaty. Czy chowacie się w tej chacie? [tak/nie]")
        wybor = input("> ").lower()
        if wybor == "tak":
            wyswietl_tekst_powoli("Schowaliście się pod łóżkiem, widzicie jak te osoby wnoszą do chaty ciało.")
            wyswietl_tekst_powoli("Zabójcy zasnęli, uciekacie z chaty, podczas ucieczki mordercy się budzą.")
            wyswietl_tekst_powoli("Zaczynają was gonić.")
            wraki()
            break
        elif wybor == "nie":
            wyswietl_tekst_powoli("Postanowiliście uciec.")
            wyswietl_tekst_powoli("Zabójcy zaczynają was gonić.")
            wraki()
            break
        else:
            wyswietl_tekst_powoli("Nie rozumiem tego wyboru. Spróbuj ponownie.")

def wzdluz_drogi():
    wyswietl_tekst_powoli("Dwoje z was poszło, a druga dwójka została w samochodzie.")
    wyswietl_tekst_powoli("Zapada zmrok. Żaden samochód nie nadjechał.")
    while True:
        wyswietl_tekst_powoli("Czy idziecie dalej? [tak/nie]")
        wybor = input("> ").lower()
        if wybor == "tak":
            wyswietl_tekst_powoli("Nagle nadjeżdża samochód, zatrzymuje się, oślepiają was światła samochodu.")
            wyswietl_tekst_powoli("Lecz dostrzegacie, że wysiadają z niego dwie postacie, jedna wyciąga coś z samochodu.")
            wyswietl_tekst_powoli("GINIESZ")
            break
        elif wybor == "nie":
            wyswietl_tekst_powoli("Wróciliście do samochodów.")
            wyswietl_tekst_powoli("Dwójki osób, która została, nie ma w samochodach.")
            wyswietl_tekst_powoli("Wokół samochodów znajdujecie pełno krwi.")
            wyswietl_tekst_powoli("Ktoś musiał ich zabić.")
            powrot_do_samochodu  ()
            break
        else:
            wyswietl_tekst_powoli("Nie rozumiem tego wyboru. Spróbuj ponownie.")

def powrot_do_samochodu (): 
    while True:
        wyswietl_tekst_powoli("Czy uciekacie do lasu?[tak/nie]")
        wybor = input(">").lower()
        if wybor == "tak":
            wyswietl_tekst_powoli("W lesie znajdujecie strażniece.")
            straznica ()
            break
        elif wybor == "nie":
            wyswietl_tekst_powoli("Chowacie się w samochodzie, lecz mordercy was znajdują.")
            wyswietl_tekst_powoli("GINIESZ")
            break
        else :
            wyswietl_tekst_powoli("Nie rozumiem tego wyboru. Spróbuj ponownie.")

def zostajesz_w_samochodzie():
    wyswietl_tekst_powoli("Zasypiacie w samochodzie, budzą was dziwne odgłosy.")
    while True:
        wyswietl_tekst_powoli("Czy zostajesz w samochodzie? [tak/nie]")
        wybor = input("> ").lower()
        if wybor == "tak":
            wyswietl_tekst_powoli("GINIESZ")
            break
        elif wybor == "nie":
            wyswietl_tekst_powoli("Ktoś zbliża się w waszą stronę.")
            while True:
                wyswietl_tekst_powoli("Uciekacie [s], czy atakujecie [a]?")
                akcja = input("> ").lower()
                if akcja in ["s", "a"]:
                    wyswietl_tekst_powoli("GINIESZ")
                    return
                else:
                    wyswietl_tekst_powoli("Nie rozumiem tego wyboru. Spróbuj ponownie.")
        else:
            wyswietl_tekst_powoli("Nie rozumiem tego wyboru. Spróbuj ponownie.")

def wraki():
    wyswietl_tekst_powoli("Docieracie do wraków samochodów, którymi podróżowały ofiary tych morderców.")
    wyswietl_tekst_powoli("Mordercy się zbliżają.")
    wyswietl_tekst_powoli("Uciekacie [u], czy jedna z was odwraca ich uwagę, a druga zakrada się do samochodu [s]?")
    while True:
        wybor = input("> ").lower()
        if wybor == "u":
            wyswietl_tekst_powoli("GINIESZ")
            break
        elif wybor == "s":
            wyswietl_tekst_powoli("Udaje się wam, odjeżdżacie samochodem, lecz zakopujecie się, dalej idziecie pieszo.")
            wraki2 ()
            break
        else:
            wyswietl_tekst_powoli("Nie rozumiem tego wyboru. Spróbuj ponownie.")

def wraki1():
    wyswietl_tekst_powoli("Uciekacie [u], czy jedna z was odwraca ich uwagę, a druga zakrada się do samochodu [s]?")
    while True:
        wybor = input("> ").lower()
        if wybor == "u":
            wyswietl_tekst_powoli("GINIESZ")
            break
        elif wybor == "s":
            wyswietl_tekst_powoli("Udaje się wam, odjeżdżacie samochodem, lecz zakopujecie się, dalej idziecie pieszo.")
            wraki2()
            break
        else:
            wyswietl_tekst_powoli("Nie rozumiem tego wyboru. Spróbuj ponownie.")

def wraki2 ():
    wyswietl_tekst_powoli("Znajdujecie strażnicę. Czy do niej wchodzicie? [tak/nie]")
    while True:
        wybor = input("> ").lower()
        if wybor == "tak":
            straznica ()
            break
        elif wybor == "nie":
            wyswietl_tekst_powoli("Mordercy was znajdują.")
            wyswietl_tekst_powoli("GINIESZ")
        else:
            wyswietl_tekst_powoli("Nie rozumiem tego wyboru. Spróbuj ponownie.")

def straznica ():
    wyswietl_tekst_powoli("W stażnicy znajdujecie radio, spróbuj wezwać pomoc.")
    # Ustawienie właściwej częstotliwości
    prawidlowa_czestotliwosc = random.randint(88, 108)  # Zakres FM: 88 - 108 MHz
    proba = 0
    znalezione = False
    wyswietl_tekst_powoli("Twoim celem jest znalezienie właściwej częstotliwości (88-108 MHz).")

    while not znalezione:
        try:
        # Pobranie częstotliwości od użytkownika
            czestotliwosc = int(input("Ustaw częstotliwość: "))
            proba += 1
        
        # Sprawdzenie częstotliwości
            if czestotliwosc < prawidlowa_czestotliwosc:
                wyswietl_tekst_powoli("Za niska! Spróbuj wyżej.")
            elif czestotliwosc > prawidlowa_czestotliwosc:
                wyswietl_tekst_powoli("Za wysoka! Spróbuj niżej.")
            else:
                wyswietl_tekst_powoli(f"Brawo! Znalazłeś właściwą częstotliwość: {prawidlowa_czestotliwosc} MHz.")
                wyswietl_tekst_powoli(f"Udało ci się w {proba} próbach.")
                znalezione = True
        except ValueError:
            wyswietl_tekst_powoli("Proszę podać liczbę z zakresu 88-108.")
   
    wyswietl_tekst_powoli("Mordercy cię usłyszeli, i wchodzą do strażnicy.")
    wyswietl_tekst_powoli("Barykadujecie się, mordercy podpalają strażnice.")
    wyswietl_tekst_powoli("Musicie skakać gałęzie pobliskich drzew.")
    wyswietl_tekst_powoli("Jeden znich zaczyna się wpinać na drzewo.")
    while True:
        wyswietl_tekst_powoli("Uciekacie [s], czy zastawiacie pułapkę odciągając gałąź tak aby go zwaliła [z]?")
        akcja = input("> ").lower()
        if akcja == ("z"):
            wyswietl_tekst_powoli("Udało się zwaliliście go.")
            straznica1 ()
            break
        elif akcja == ("s"):
            wyswietl_tekst_powoli("Morderca was dogania.")
            wyswietl_tekst_powoli("GINIESZ")      
            break
        else:
            wyswietl_tekst_powoli("Nie rozumiem tego wyboru. Spróbuj ponownie.")

def straznica1 ():
    wyswietl_tekst_powoli("Uciekliście nim.")
    while True:
        wyswietl_tekst_powoli("Znajdujecie jaskinie za wodospadem. Czy się w niej chowacie? [tak]/[nie]")
        wybor = input("> ").lower() 
        if wybor == ("tak"):
            wyswietl_tekst_powoli("Schowaliście się w jaskini, widziecie jak mardercy przechodzą obok was")
            jaskinia ()
            break
        elif wybor == ("nie"):
            wyswietl_tekst_powoli("GINIESZ")
            break
        else :
             wyswietl_tekst_powoli("Nie rozumiem tego wyboru. Spróbuj ponownie.")

def jaskinia():
    wyswietl_tekst_powoli("Przeczekaliście noc, rano wyruszacie, docieracie do drogi.")
    wyswietl_tekst_powoli("Drogą jedzie wezwana wcześniej policja.")
    
    wydarzenie = random.choice(["mordercy", "porwanie"])
    
    if wydarzenie == "mordercy":
        atak_mordercow()
    elif wydarzenie == "porwanie":
        porwanie_towarzyszki()

def atak_mordercow():
    wyswietl_tekst_powoli("Nagle z lasu wyskakują mordercy! Pomoc zostaje zaatakowana!")
    wyswietl_tekst_powoli("Nie macie wyboru - musicie walczyć lub uciekać.")
    while True:
        wybor = input("Co robisz? (walcz/uciekaj): ").lower()
        if wybor == "walcz":
            wyswietl_tekst_powoli("Walczycie z mordercami... Udało się ich pokonać, ale policjanci zostali zabici.")
            zakoncz_gre ()
            break
        elif wybor == "uciekaj":
            wyswietl_tekst_powoli("Mordercy was doganiają")
            wyswietl_tekst_powoli("GINIESZ")
            break
        else:
            wyswietl_tekst_powoli("Nie rozumiem tego wyboru. Spróbuj ponownie.")

def porwanie_towarzyszki():
    wyswietl_tekst_powoli("Z lasu wybiegają zabujcy i porywają twoją towarzyszkę!")
    wyswietl_tekst_powoli("Masz wybór: podjąć się jej ratowania lub uciec samemu.")
    while True:
        wybor = input("Co robisz? (ratuj/uciekaj): ").lower()
        if wybor == "ratuj":
            wyswietl_tekst_powoli("Postanawiasz ją uratować. Wyruszasz za zabujcami, do ich chaty...")
            wyswietl_tekst_powoli("Udało ci się ją uratować! Możecie razem wrócić do domu.")
            zakoncz_gre ()
            break
        elif wybor == "uciekaj":
            wyswietl_tekst_powoli("Uciekasz, zostawiając towarzyszkę na pastwę losu. Nigdy nie wybaczysz sobie tej decyzji.")
            wyswietl_tekst_powoli("Gra zakończona porażką.")
            break
        else:
            wyswietl_tekst_powoli("Nie rozumiem tego wyboru. Spróbuj ponownie.")

def zakoncz_gre():
    wyswietl_tekst_powoli("Wsiadacie do samochodu i odjeżdżacie w stronę horyzontu.")
    wyswietl_tekst_powoli("Gra zakończona sukcesem. Gratulacje!")    
    
def main():
    while True:
        wyswietl_tekst_powoli ("Czy chcesz zagrać w grę? (tak/nie): ")
        odp = input("> ").strip().lower()
        if odp == "tak":
            start()
        elif odp == "nie":
            break
        else:
            wyswietl_tekst_powoli("Proszę odpowiedzieć 'tak' lub 'nie'.")

if __name__ == "__main__":
    main()
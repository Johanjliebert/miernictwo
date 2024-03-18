# This is a sample Python script.
import math


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def wczytaj_plik(nazwa_pliku):
    zwierzeta = list()
    try:
        # Wczytanie danych z pliku
        with open(nazwa_pliku, 'r') as file:
            # Odczytanie zawartości pliku
            lines = file.readlines()
            for line in lines:
                zwierzeta.append(float(line))

    except FileNotFoundError:
        print("plik nie znaleziony, podaj dane (podaj zero jako ostatnią liczbe)")
        x=1
        while(x!=0):
            x=input()
            if (x!=0):
                zwierzeta.append(float(x))
        return zwierzeta
    except ValueError as ve:
        print("Błąd w pliku:", ve)
    except Exception as e:
        print("Wystąpił nieznany błąd:", e)

    return zwierzeta

def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    print("0 - koniec programu")
    print("1 - wartosc srednia")
    print("2 - odchylenie standardowe")
    print("3 - odchylenie srednie")
    print("4 - polacz pliki")
    print("5 - niepewnosc calkowita")
    #co=input("Co chcesz obliczyc?")
    #while(co!=0):
    for co in range(5):
        suma=0
        ilosc=0
        match co:
            case 1:
                print("wczytywanie wartosci pomiarow...")
                pomiary=wczytaj_plik("wartosci.txt")
                for pomiar in pomiary:
                    suma+=pomiar
                    ilosc+=1
                pliksrednia=open("srednia.txt",mode='w')
                pliksrednia.write(str(suma/ilosc))
                pliksrednia.close()
            case 2:
                wartosci=wczytaj_plik("wartosci.txt")
                srednia=wczytaj_plik("srednia.txt")
                for wartosc in wartosci:
                    ilosc+=1
                    suma+=(wartosc-srednia[0])*(wartosc-srednia[0])
                plikodchyl=open("odchyleniestandard.txt", mode='w')
                plikodchyl.write(str(math.sqrt(suma/ilosc-1)))
                plikodchyl.close()
                plikilosc=open("ilosc.txt",mode='w')
                plikilosc.write(str(ilosc))
                plikilosc.close()
            case 3:
                odchyl=wczytaj_plik("odchyleniestandard.txt")
                odchylsr=open("odchylsr.txt",mode='w')
                ilosc=wczytaj_plik("ilosc.txt")
                odchylsr.write(str(odchyl[0]/math.sqrt(ilosc[0])))
                odchylsr.close()
            case 4:
                zapisz=open("dane.txt",mode='w')
                zapisz.write("srednia = "+str(wczytaj_plik("srednia.txt")))
                zapisz.write("odchylenie standardowe = "+str(wczytaj_plik("odchyleniestandard.txt")))
                zapisz.write("odchylenie srednie = "+str(wczytaj_plik("odchylsr.txt")))
                zapisz.close()
        #co = input("Co chcesz obliczyc?")

print_hi()


# Press the green button in the gutter to run the script.


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
    print("1 - odchylenie standardowe+srednie")
    print("2 - rezystancja calkowita")
    print("3 - niepewnosc obliczen")
    co=input("Co chcesz obliczyc?")
    #while(co!=0):
    for z in range(1):
        suma=0
        ilosc=0
        match co:
            case 1:
                srednia=0
                print("wczytywanie wartosci pomiarow...")
                pomiary=wczytaj_plik("wartosci.txt")
                for pomiar in pomiary:
                    srednia+=pomiar
                    ilosc+=1
                srednia/=ilosc
                for wartosc in pomiary:
                    suma+=(wartosc-srednia)*(wartosc-srednia)
                odchyl=math.sqrt(suma/(ilosc-1))


                odchylsr=odchyl/math.sqrt(ilosc)

                zapisz=open("dane.txt",mode='w')
                #zapisz.write("srednia = ")
                zapisz.write(str(srednia)+"\n")
                #zapisz.write("odchylenie standardowe = ")
                zapisz.write(str(odchyl)+"\n")
                #zapisz.write("odchylenie srednie = ")
                zapisz.write(str(odchylsr)+"\n")
                zapisz.close()
            case 2:
                dane=wczytaj_plik("dane.txt")
                rizz=wczytaj_plik("rezystancja.txt")
                rez=open("rezystancja_calkowita.txt",mode='w')
                rez.write(str(math.sqrt(dane[1]*dane[1]+rizz[0]*rizz[0]/3+rizz[1]*rizz[1]/3)))
            case '3':
                wartosci=wczytaj_plik("wartosci.txt")
                niepewnosc = open("niepewnosc.txt",mode='w')
                for wartosc in wartosci:
                    x=0.01
                    if(wartosc<2):
                        x=0.001
                    if(wartosc<0.2):
                        x=0.00001
                    niepewnosc.write(str(wartosc/1000+x)+"\n")
                niepewnosc.close()
        #co = input("Co chcesz obliczyc?")


print_hi()


# Press the green button in the gutter to run the script.


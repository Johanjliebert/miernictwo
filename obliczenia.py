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
    print("2 - niepewnosc calkowita")
    print("3 - srednia wazona")
    print("4 - niepewnosc obliczen")
    co=input("Co chcesz obliczyc?")
    #while(co!=0):
    for z in range(1):
        suma=0
        ilosc=0
        match co:
            case '1':
                srednia=0
                print("wczytywanie wartosci pomiarow...")
                pomiary=wczytaj_plik("wartosci1.txt")
                for pomiar in pomiary:
                    srednia+=pomiar
                    ilosc+=1
                srednia/=ilosc
                for wartosc in pomiary:
                    suma+=(wartosc-srednia)*(wartosc-srednia)
                odchyl=math.sqrt(suma/(ilosc-1))


                odchylsr=odchyl/math.sqrt(ilosc)

                zapisz=open("dane1.txt",mode='w')
                zapisz.write(str(srednia)+"\n")
                zapisz.write(str(odchyl)+"\n")
                zapisz.write(str(odchylsr)+"\n")
                zapisz.close()

                srednia=0
                ilosc=0
                print("wczytywanie wartosci pomiarow...")
                pomiary=wczytaj_plik("wartosci2.txt")
                for pomiar in pomiary:
                    srednia+=pomiar
                    ilosc+=1
                srednia/=ilosc
                for wartosc in pomiary:
                    suma+=(wartosc-srednia)*(wartosc-srednia)
                odchyl=math.sqrt(suma/(ilosc-1))


                odchylsr=odchyl/math.sqrt(ilosc)

                zapisz=open("dane2.txt",mode='w')
                zapisz.write(str(srednia)+"\n")
                zapisz.write(str(odchyl)+"\n")
                zapisz.write(str(odchylsr)+"\n")
                zapisz.close()
            case '2':
                dane=wczytaj_plik("dane1.txt")
                rizz=wczytaj_plik("rezystancja1.txt")
                np=open("niepewnosc_calkowita1.txt",mode='w')
                np.write(str(math.sqrt(dane[1]*dane[1]+rizz[0]*rizz[0]/3+rizz[1]*rizz[1]/3)))
                np.close()
                dane=wczytaj_plik("dane2.txt")
                rizz=wczytaj_plik("rezystancja2.txt")
                np=open("niepewnosc_calkowita2.txt",mode='w')
                np.write(str(math.sqrt(dane[1]*dane[1]+rizz[0]*rizz[0]/3+rizz[1]*rizz[1]/3)))
                np.close()
            case '3':
                waga=list()
                listsrednia=list()
                listsrednia.append(wczytaj_plik("dane1.txt")[0])
                listsrednia.append(wczytaj_plik("dane2.txt")[0])
                waga.append(wczytaj_plik("niepewnosc_calkowita1.txt")[0])
                waga.append(wczytaj_plik("niepewnosc_calkowita2.txt")[0])
                wait=open("waga.txt", mode='w')
                waga[0]=1/(waga[0]*waga[0])
                waga[1]=1/(waga[1]*waga[1])
                wait.write(str(waga[0])+"\n")
                wait.write(str(waga[1])+"\n")
                wait.write(str((waga[0]*listsrednia[0]+waga[1]*listsrednia[1])/(waga[0]+waga[1]))+"\n")
                wait.write(str(math.sqrt(1/(waga[0]+waga[1]))))
            case '4':
                wartosci=wczytaj_plik("wartosci.txt")
                niepewnosc = open("niepewnosc.txt",mode='w')
                for wartosc in wartosci:
                    suma=0
                    wart=str(wartosc)
                    if(wartosc>10000):
                        suma+=int(wart[0])*10
                        suma+=int(wart[1])*1
                        suma+=int(wart[2])*0.5
                        suma+=int(wart[3])*0.01
                        suma+=int(wart[4])*0.002
                    else:
                        suma+=int(wart[0])*1
                        suma+=int(wart[1])*0.5
                        suma+=int(wart[2])*0.01
                        suma+=int(wart[3])*0.002
                    niepewnosc.write(str(suma)+"\n")
                niepewnosc.close()
        #co = input("Co chcesz obliczyc?")


print_hi()


# Press the green button in the gutter to run the script.


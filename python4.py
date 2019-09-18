import os, time

def start_menu():
    naam = input("Hoe heet je? ")
    print("=-="*11)
    print("Welkom " + naam + " bij mijn overhoor programma!")
    print("     Type O voor een overhoring")
    print("     Type R om een vertaling weg te halen")
    print("     Type T om een vertaling toe te voegen")
    print("     Type L om de woordelijsten te zien")
    print("     Type Q om af te sluiten")
    print("=-="*11)

def engels_lijst(engels):
    for key, value in engels.items():
        print(key + " - " + value)

def duits_lijst(duits):
    for key, value in duits.items():
        print(key + " - " + value)
def frans_lijst(frans):
    for key, value in frans.items():
        print(key + " - " + value)


def main():
    engels = {"apple": "appel"}
    frans = {"pommes": "patat"}
    duits = {"nein": "nee"}
    start_menu()
    programma =  True
    while programma:
        keuze =  input("Wat is je keuze? ").lower()

        if keuze == "o":
            welke_o = input("welke woordenlijst wil je overhoord hebben ")
            if welke_o == "en-nl":
                print("1")
            elif welke_o == "du-nl":
                    print("2")
            elif welke_o == "fr-nl":
                        print("1")
            elif welke_o == "q":
                main()
                os.system('cls')
            else:
                print("Kies een van de aangegeven woordenlijsten")

        if keuze == "q":
            programma = False
            os.system('cls')

        if keuze == "l":
            print("=-="*6)
            print("Engelse lijst:")
            print("")
            engels_lijst(engels)
            print("=-="*6)

            print("Franse lijst:")
            print("")
            frans_lijst(frans)
            print("=-="*6)

            print("Duitse lijst:")
            print("")
            duits_lijst(duits)
            print("=-="*6)

        else:
            print("voer een van de aangegeven letters in!")



if __name__ == "__main__":
    main()

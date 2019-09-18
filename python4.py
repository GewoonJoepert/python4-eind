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

def voeg_engels_woord_toe(engels):
    woord = input("type een woord in ")
    vertaling = input("voer de vertaling in ")
    engels[woord] = vertaling

def voeg_frans_woord_toe(frans):
    woord1 = input("type een woord in ")
    vertaling1 = input("voer de vertaling in ")
    frans[woord1] = vertaling1

def voeg_duits_woord_toe(duits):
    woord2 = input("type een woord in ")
    vertaling2 = input("voer de vertaling in ")
    duits[woord2] = vertaling2

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

        elif keuze == "q":
            programma = False
            os.system('cls')

        elif keuze == "l":
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

        elif keuze == "t":
            keuze_t = input("aan welke lijst wil je een vertaling toevoegen? kies uit: en-nl, du-nl, fr-nl ")
            if keuze_t == "en-nl":
                voeg_engels_woord_toe(engels)
                engels_lijst(engels)
            elif keuze-t == "fr-nl":
                    voeg_frans_woord_toe(frans)
                    frans_lijst(frans)
            elif keuze_t == "du-nl":
                    voeg_duits_woord_toe(duits)
                    duits_lijst(duits)
            else:
                print("voer een van de aangegeven lijsten in")

        else:
            print("voer een van de aangegeven letters in!")


if __name__ == "__main__":
    main()

import os, time


def start_menu():
    naam = input("Hoe heet je? ")
    os.system('cls')
    print("=-="*15)
    print("| {:41} |".format("Welkom " + naam + " bij mijn overhoor programma!"))
    print("| {:41} |".format("  Type O voor een overhoring"))
    print("| {:41} |".format("  Type R om een vertaling weg te halen"))
    print("| {:41} |".format("  Type T om een vertaling toe te voegen"))
    print("| {:41} |".format("  Type L om de woordelijsten te zien"))
    print("| {:41} |".format("  Type Q om af te sluiten"))
    print("=-="*15)
#print("| Woord: {:14} Vertaling: {:22} |".format(woord, vertaling))

def print_woordenlijst(woordenlijst):
    for key, value in woordenlijst.items():
        print(key + " - " + value)


def print_woordenlijsten(woordenlijsten):
    for lijst in woordenlijsten:
        print_woordenlijst(lijst)


def vraag_en_voeg_woorden_toe(woordenlijst):
    woord = input("type een woord in ")
    vertaling = input("voer de vertaling in ")
    woordenlijst[woord] = vertaling


def remove_woord(woord):
    del woord[input("vul het woord in ")]


def overhoor_keuze(welke_o):
    if welke_o == "en-nl":
        print("1")
    elif welke_o == "du-nl":
        print("2")
    elif welke_o == "fr-nl":
        print("3")
    elif welke_o == "q":
        main()
        os.system('cls')
    else:
        print("Kies een van de aangegeven woordenlijsten")


def main():
    engels = {"apple": "appel"}
    frans = {"pommes": "patat"}
    duits = {"nein": "nee"}
    start_menu()
    programma =  True

    while programma:
        keuze =  input("Wat is je keuze? ").lower()

        if keuze == "o":
            welke_o = input("welke woordenlijst wil je overhoord hebben? kies uit: en-nl, du-nl & fr-nl ")
            overhoor_keuze(welke_o)

        elif keuze == "q":
            programma = False
            os.system('cls')

        elif keuze == "l":
            print_woordenlijsten([engels, duits, frans])

        elif keuze == "t":
            keuze_t = input("aan welke lijst wil je een vertaling toevoegen? kies uit: en-nl, du-nl & fr-nl ")
            if keuze_t == "en-nl":
                vraag_en_voeg_woorden_toe(engels)
                print_woordenlijst(engels)
            elif keuze_t == "fr-nl":
                vraag_en_voeg_woorden_toe(frans)
                print_woordenlijst(frans)
            elif keuze_t == "du-nl":
                vraag_en_voeg_woorden_toe(duits)
                print_woordenlijst(duits)
            else:
                print("voer een van de aangegeven lijsten in")
                time.sleep(2)
                os.system('cls')

        elif keuze == "r":
            keuze_r = input("uit welke lijst wil je iets verwijderen? kies uit: en-nl, du-nl & fr-nl ")
            if keuze_r == "en-nl":
                print_woordenlijst(engels)
                remove_woord(engels)
                print_woordenlijst(engels)
            elif keuze_r == "du-nl":
                print_woordenlijst(duits)
                remove_woord(duits)
                print_woordenlijst(duits)
            elif keuze_r == "fr-nl":
                print_woordenlijst(frans)
                remove_woord(frans)
                print_woordenlijst(frans)
            else:
                print("voer een van de aangegeven lijsten in")
                time.sleep(2)
                os.system('cls')

        else:
            print("voer een van de aangegeven letters in!")
            time.sleep(2)
            os.system('cls')

if __name__ == "__main__":
    main()

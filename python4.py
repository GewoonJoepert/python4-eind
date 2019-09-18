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

def main():
    start_menu()
    programma =  True
    while programma:
        keuze =  input("Wat is je keuze? ").lower()

        if keuze == "o":
            welke_o = input("welke woordenlijst wil je overhoord hebben ")
            if welke_o == "en-nl":
                print("3")
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
            for key, value in woordlijsten.items():
                print(key + " - " + value)

        else:
            print("voer een van de aangegeven letters in!")



if __name__ == "__main__":
    main()

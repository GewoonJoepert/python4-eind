import os, time

def start_menu():
    naam = input("Hoe heet je? ")
    print("=-="*11)
    print("Welkom " + naam + " bij mijn overhoor programma!")
    print("     Type D om door te gaan")
    print("     Type R om iets weg te halen")
    print("     Type L om de lijst te laten zien")
    print("     Type Q om af te sluiten")
    print("=-="*11)
    
def main():
    start_menu()

if __name__ == "__main__":
    main()

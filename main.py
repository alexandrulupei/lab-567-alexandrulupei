from Logic.CRUD import adaugareVanzare
from Tests.testAll import runalltests
from UI.console import runMenu

def main():
    runalltests()
    lista = []
    lista = adaugareVanzare("1", "Moarte pe nil", "politist", 100, "gold", lista)
    lista = adaugareVanzare("2", "Criminalul ABC", "politist", 1000, "silver", lista)
    runMenu(lista)

main()
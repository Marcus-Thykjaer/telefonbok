#lager en tom telefonbok liste
telefonbok = []
#lager to personer og legger til dem i telefonboken
person1 = {"navn":"sebastian","telefonnummer": "1234567"}
person2 = {"navn":"marcus", "telefonnummer":"12356784"}

#legger til person1 og person2 i telefonboken ved bruk av append
telefonbok.append(person1)
telefonbok.append(person2)

#vi lager en funksjon til
def vis_alle():
    for person in telefonbok:
        print(F"navn: {person['navn']}, telefonnummer: {person['telefonnummer']}") #f-string for å få ut navn og telefonnummer fra person

#vi kaller på funksjonen
vis_alle()



def legg_til():
    navn= input("skriv inn navn: ")
    telefonnummer = input("skriv inn telefonnummer: ")
    person = {"navn": navn, "telefonnummer": telefonnummer}
    telefonbok.append(person)                           #legger til personen bruker laget med append
    print(f"{navn} ble lagt til i telefonboka.")

#vi kaller på funksjonen
legg_til()

def søk():
    navn_søk = input("Skriv inn navnet du vil søke etter: ").lower()
    funnet = False

    for person in telefonbok:
        if person["navn"].lower() == navn_søk:
            print(f"Fant {person['navn']} med telefonnummer: {person['telefonnummer']}.")
            funnet = True
            break
    
    if not funnet:
        print(f"{navn_søk} ble ikke funnet i telefonboka.")

# kaller på funksjonen
søk()

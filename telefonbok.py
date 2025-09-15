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




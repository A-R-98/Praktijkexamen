def pensioen_medewerker():
    if leeftijd >=65:
        return basispensioen[0]
    if leeftijd >=65 and leeftijd <70:
        return leeftijdsbonus[0]

def pensioen_zelfstandige():
    if leeftijd >=65:
        return basispensioen[1]
    if leeftijd >=65 and leeftijd <70:
        return leeftijdsbonus[1]
    
def pensioen_ambtenaar():
    if leeftijd >=65:
        return basispensioen[2]
    if leeftijd >=65 and leeftijd <70:
        return leeftijdsbonus[2]
    
basispensioen=[350,300,370]
leeftijdsbonus=[370,315,395]

leeftijd=int(input("Wat is je leeftijd? Voer het aantal jaren in:"))
rest_tijd=65-leeftijd
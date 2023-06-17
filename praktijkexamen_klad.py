leeftijd=int(input("Wat is je leeftijd? Voer het aantal jaren in:"))
rest_tijd=65-leeftijd

werkstatuut= ["medewerker", "zelfstandige", "ambtenaar"]
werkstatuut=input("Wat is je werkstatuut? Voer in: medewerker, zelfstandige of ambtenaar:")

def basispensioen(werkstatuut):
    if werkstatuut["medewerker"]:
        return 350
    if werkstatuut["zelfstandige"]:
        return 300
    if werkstatuut ["ambtenaar"]:
        return 370    

def leeftijdsbonus(werkstatuut):
    if werkstatuut["medewerker"]:
        return 370
    if werkstatuut["zelfstandige"]:
        return 315
    if werkstatuut ["ambtenaar"]:
        return 395

def pensioengerechtigheid():    
    if leeftijd <65:
        print (f"Van werken word je gelukkig, je mag nog {rest_tijd} jaar genieten van je baan.")    
    else:
        if leeftijd <70:
            print (f"Je krijgt €{basispensioen} per week.")
        else:
            print (f"Je krijgt €{leeftijdsbonus} per week.")
        
print (pensioengerechtigheid())
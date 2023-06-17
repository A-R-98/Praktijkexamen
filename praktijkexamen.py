leeftijd=int(input("Wat is uw leeftijd? Voer het aantal jaren in: \n"))

#De variabele 'rest_tijd' is het aantal jaren dat de gebruiker nog moet werken tot de pensioengerechtigde leeftijd van 65 jaar behaald is.
rest_tijd=65-leeftijd

werkstatuut=input("Wat is uw werkstatuut? \n Vul in 1 voor medewerker \n Vul in 2 voor zelfstandige \n Vul in 3 voor ambtenaar: \n")
werkstatuut=int(werkstatuut)                

#De lists 'basispensioen' en 'leeftijdsbonus' bevatten elk drie elementen die de wekelijks te ontvangen pensioenbedragen voor respectievelijk medewerkers, zelfstandigen en ambtenaren representeren. 
basispensioen=[350,300,370]
leeftijdsbonus=[370,315,395] #De variabele 'leeftijdsbonus is het wekelijks te ontvangen pensioenbedrag voor gebruikers vanaf 70 jaar.


def pensioen_uitkeer(leeftijd,werkstatuut):
    if leeftijd <65:
        return (f"Van werken wordt u gelukkig, u mag nog {rest_tijd} jaar genieten van uw baan.")
    else:
        if leeftijd >=65 and leeftijd <70:
            if werkstatuut ==1:
                return (f"U krijgt €{basispensioen [0]} per week.")
            if werkstatuut ==2:
                return (f"U krijgt €{basispensioen [1]} per week.")
            if werkstatuut ==3:
                return (f"U krijgt €{basispensioen [2]} per week.")
        
        if leeftijd >=70:
            if werkstatuut ==1:
                return (f"U krijgt €{leeftijdsbonus [0]} per week.")
            if werkstatuut ==2:
                return (f"U krijgt €{leeftijdsbonus [1]} per week.")
            if werkstatuut ==3:
                return (f"U krijgt €{leeftijdsbonus [2]} per week.")

print (pensioen_uitkeer(leeftijd, werkstatuut))

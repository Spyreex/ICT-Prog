def standaardprijs(afstandKM):
    prijs = 0
    if afstandKM <= 50:
        prijs = afstandKM*0.8
    else:
        prijs = afstandKM*0.6 + 15
    return prijs

def ritprijs(leeftijd,weekendrit,afstandKM):
    prijs = standaardprijs(afstandKM)
    if leeftijd < 12 or leeftijd >= 65:
        if weekendrit == True:
            prijs = round(prijs*0.65,2)
        else:
            prijs = round(prijs*0.7,2)
    else:
        if weekendrit == True:
            prijs = round(prijs*0.60,2)
    print('De betalen prijs is €' + str(prijs))

for x in range(0,50,1):                     #er wordt hier te veel uitgeprint dat het begin verwijderd wordt, daarom heb ik er 2 gemaakt (0-50 e 50-100)
    for y in range(0,50,1):
        leeftijd = y
        afstandKM = x
        ritprijs(y,True,x)
        print('Leeftijd =',y)
        print('Afstand =',x)
        print('Wel Weekendreis')
        print('')
        ritprijs(y,False,x)
        print('Leeftijd =', y)
        print('Afstand =', x)
        print('Geen Weekendreis')
        print('')

for x in range(50,100,1):
    for y in range(50,100,1):
        leeftijd = y
        afstandKM = x
        ritprijs(y,True,x)
        print('Leeftijd =',y)
        print('Afstand =',x)
        print('Wel Weekendreis')
        print('')
        ritprijs(y,False,x)
        print('Leeftijd =', y)
        print('Afstand =', x)
        print('Geen Weekendreis')
        print('')
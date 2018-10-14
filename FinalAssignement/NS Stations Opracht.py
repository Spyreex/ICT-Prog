stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
def inlezen_beginstation(stations):
    beginstation = input('Wat is uw beginstation: ')
    while beginstation not in stations:
        print('Wat u heeft ingevoerd bestaat niet')
        beginstation = input('Wat is uw beginstation: ')
    return beginstation

def inlezen_eindstation(stations, beginstation):
    eindstation = input('Wat is uw eindstation: ')
    while True:
        if eindstation not in stations:
            print('Wat u heeft ingevoerd bestaat niet')
            eindstation = input('Wat is uw eindstation: ')
        elif stations.index(eindstation) <= stations.index(beginstation):
            print('De ingevoerde eindstation is niet mogelijk, graag een hoger eindstation kiezen: ')
            eindstation = input('Wat is uw eindstation: ')
        else:
            return eindstation
        continue

def omroepen_reis(stations, beginstation, eindstation):
    x = stations.index(beginstation)
    y = stations.index(eindstation)
    print('\nHet beginstation',beginstation, 'is het',str(x+1)+'e station in het traject.')
    print('Het eindstation', eindstation, 'is het',str(y+1) + 'e station in het traject.')
    print('De afstand bedraagt',str(y-x),'station(s).')
    print('De prijs van het kaartje is',str((y-x)*5),'euro.\n')

    print('U stapt in de trein in:',beginstation)
    for z in range(x+1,y):
        print('-',stations[z])
    print('U stapt uit in:',eindstation)

beginstation = inlezen_beginstation(stations)

eindstation = inlezen_eindstation(stations, beginstation)

omroepen_reis(stations, beginstation, eindstation)

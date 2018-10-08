def toon_aantal_kluizen_vrij():
    infile = open('kluizen.txt','r')
    vrij = (12 - len(infile.readlines()))
    infile.close()
    return 'Er zijn nog',vrij,'kluizen vrij'

def nieuwe_kluis():
    kluislijst = [1,2,3,4,5,6,7,8,9,10,11,12]
    rfile = open('kluizen.txt', 'r')
    lines = rfile.readlines()
    if len(lines) > 12:
        rfile.close()
        return 'Er zijn helaas geen kluizen beschikbaar'
    else:
        for line in lines:
            line = line.split(';')
            kluislijst.remove(int(line[0]))
        nieuw = input('Voer kluiscode in: ')
        rfile.close()
        afile = open('kluizen.txt', 'a')
        eerste_kluis = kluislijst[0]
        if len(lines) != 0:
            afile.write('\n')
        afile.write(str(eerste_kluis)+';'+nieuw)
        afile.close()
        return 'Jouw kluisnummer:',str(eerste_kluis)

def kluis_openen():
    counter = 0
    kluisnummer = input('Wat is uw kluisnummer: ')
    kluiscode = input('Wat is uw kluiscode: ')
    rfile = open('kluizen.txt', 'r')
    lines = rfile.readlines()
    for line in lines:
        line = line.split(';')
        wachtwoord = line[1].strip('\n')
        if kluisnummer == line[0]:
            if kluiscode == wachtwoord:
                counter += 1
    rfile.close()
    if counter == 1:
        return 'Dit is correct'
    else:
        return 'Kluisnummer/Kluiscode is incorrect'

def bagagekluizen():
    while True:
        x = input('1: Ik wil weten hoeveel kluizen nog vrij zijn\n'
        '2: Ik wil een nieuwe kluis\n'
        '3: Ik wil even iets uit mijn kluis halen\n'
        '4: Afsluiten\n'
        'Keuze: ')
        if x == '1':
            print(toon_aantal_kluizen_vrij())
        elif x == '2':
            print(nieuwe_kluis())
        elif x == '3':
            print(kluis_openen())
        elif x == '4':
            exit()
        else:
            print('U heeft iets ingevoerd dat niet kan')
            continue

bagagekluizen()

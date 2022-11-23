import csv
import sys
#Hier CSV-Datei einlesen
dateiCSV = sys.argv[1]
#dateiCSV = 'subject-info-i.csv'
with open(dateiCSV) as csvdatei:
    reader = csv.reader(csvdatei, delimiter=',')
    col = 0
    summe = 0
    for row in reader:
        if col == 0:
            print(f'{", ".join(row)}')
        else:
            #print(f'Subject-Number: {row[0]} \t| Age: {row[1]} \t| Height/cm: {row[2]} \t| Weight/kg: {row[3]}.')
            summe = summe + int(row[1])
        col += 1

#Hier Durchschnittsalter berechnen
#Aufgabe A:
average = summe / (col - 1)
print("Aufgabe A: Was ist das Durchschnittsalter der Patienten?")
print("Das Durchscnittsalter ist: ", average)

#Hier Textdateien einlesen
prozentsatzGesamt = 0
prozentsatzGesamtRuckenlage = 0
prozentsatzGesamtSeitenlage = 0
prozentsatzGesamtRuckenlageX = 0
prozentsatzGesamtSeitenlageX = 0
prozentsatzGesamtX = 0
prozentsatzSeitenlage = 0
prozentsatzRuckenlage = 0

obereNeigungNull = 0
untereNeigungNull = 0
obereNeigung60 = 0
untereNeigung60 = 0

untereGesamtNull = 0
obereGesamtNull = 0
untereGesamt60 = 0
obereGesamt60 = 0

supineNeigungNullobere = 0
supineNeigung60obere = 0
supineNeigungNulluntere = 0
supineNeigung60untere = 0

leftRightNullobere = 0
leftRight60obere = 0
leftRightNulluntere = 0
leftRight60untere = 0

obereNeigungNullLeftRight =0
untereNeigungNullLeftRight = 0

untereGesamtNullLeftRight = 0
obereGesamtNullLeftRight = 0


j = 1
while j < 14:
    i = 1
    while i < 18:
        pfad = sys.argv[2] + str(j) + "/"
        #pfad = "C:\\Users\\adidr\\Desktop\\UNI\\Digital Health\\a-pressure-map-dataset-for-in-bed-posture-classification-1.0.0\\experiment-i\\S" + str(j) +"\\"
        string = pfad + str(i) + '.txt'
        datei2 = open(string,'r')
        #print(datei2.read())
        count = 0
        liste = []
        neuListe = []
        for zeile in datei2:
            space = 0
            t = zeile.rsplit("\t")
            neuListe.append(t)
            for x in zeile:
                if x == '\n':
                    count += 1
                if x == '\t':
                    space += 1
                if x != '\n' and x != '\t':
                    liste.append(int(x))
        finalListe = []
        for x in neuListe:
            finalListe = finalListe + x
        counter = 0
        counterNichtNull = 0
        for x in finalListe:
            if x != '\n':
                counter += 1
            if x != '0':
                counterNichtNull += 1

        #hier Aufgabe B: Wie viele Messungen in Rückenlage
        anzahlNullen = counter - counterNichtNull
        haelfte = counter // 2
        viertel = haelfte // 2
        dreiviertel = counter * 0.7

        # hier aufgabe C: durchschnittlicher Prozentsatz der Matte über 200
        bigger200 = 0
        for x in finalListe:
            if x != '\n':
                if int(x) >= 200:
                    bigger200 += 1
        #Aufgabe C1
        #Rückenlage messen
        if i == 1 or i > 7 and i < 18:
            prozentsatzRuckenlage = (bigger200 / counter) * 100
            #print("Prozentsatz von Matte " + str(i) + " in Rückenlage: " + str(prozentsatzRuckenlage))
        #Aufgabe C2
        #Seitenlage messen
        if i > 1 and i < 8:
            prozentsatzSeitenlage = (bigger200 / counter) * 100
            #print("Prozentsatz von Matte " + str(i) + " in Seitenlage: " + str(prozentsatzSeitenlage))

        #Aufgabe C3 obere und untere Mattenhälfte
        obere = 0
        untere = 0
        lauf = 0
        for x in finalListe:
            lauf += 1
            if x != '\n' and lauf < haelfte:
                if x != '0':
                    if int(x) > 200:
                        obere += 1
            if x != '\n' and lauf > haelfte and lauf < counter:
                if x != '0':
                    if int(x) > 200:
                        untere += 1
        #if i > 0 and i < 15:
        #    prozentsatzObere = (obere/haelfte) * 100 # vorher anstatt haelfte hatte ich counter
        #    prozentsatzUntere = (untere/haelfte) * 100 #vorher anstatt haelfte hatte ich counter
            #obereNeigungNull += prozentsatzObere
            #untereNeigungNull += prozentsatzUntere
        #supine bed inclination 0
        if i == 1 or i > 7 and i <13:
            supineNeigungNullobere = (obere/haelfte) * 100
            supineNeigungNulluntere = (untere/haelfte) * 100
            obereNeigungNull += supineNeigungNullobere
            untereNeigungNull += supineNeigungNulluntere
        #supine bed inclination 60
        if i == 17:
            supineNeigung60obere = (obere / haelfte) * 100
            supineNeigung60untere = (untere / haelfte) * 100
            obereNeigung60 += supineNeigung60obere
            untereNeigung60 += supineNeigung60untere

        #left/right bed inclination 0
        if i > 1 and i <8 or i == 13 or i == 14:
            leftRightNullobere = (obere / haelfte) * 100
            leftRightNulluntere = (untere / haelfte) * 100
            obereNeigungNullLeftRight += leftRightNullobere
            untereNeigungNullLeftRight += leftRightNulluntere


        if i == 1 or i > 7 and i < 18:
            prozentsatzGesamtRuckenlage += prozentsatzRuckenlage
        #print("Prozent Rücken: ", prozentsatzGesamtRuckenlage)
        if i > 1 and i < 8:
            prozentsatzGesamtSeitenlage += prozentsatzSeitenlage
        i = i + 1
    prozentsatzGesamtRuckenlage = prozentsatzGesamtRuckenlage / 9
    prozentsatzGesamtSeitenlage = prozentsatzGesamtSeitenlage / 8

    prozentsatzGesamtRuckenlageX += prozentsatzGesamtRuckenlage
    prozentsatzGesamtSeitenlageX += prozentsatzGesamtSeitenlage

    #supine position bed inclination 0
    untereNeigungNull = untereNeigungNull / 6
    untereGesamtNull += untereNeigungNull
    obereNeigungNull = obereNeigungNull / 6
    obereGesamtNull += obereNeigungNull
    #supine position bed inclination 60
    untereNeigung60 = untereNeigung60
    untereGesamt60 += untereNeigung60
    obereNeigung60 = obereNeigung60
    obereGesamt60 += obereNeigung60
    #left/right position bed inclination 0
    untereNeigungNullLeftRight = untereNeigungNullLeftRight / 8
    untereGesamtNullLeftRight += untereNeigungNullLeftRight
    obereNeigungNullLeftRight = obereNeigungNullLeftRight / 8
    obereGesamtNullLeftRight += obereNeigungNullLeftRight

    j = j + 1

#Positionen in Rückenlage = 9, für Experiment 1
ruckenlage = 9
#Positionen in Seitenlage = 8, für Experiment 1
seitenlage = 8
patienten = 13
frames = 120
#Aufgabe B: Wie viele Messungen in Rückenlage: Positionen in Rückenlage * Patienten * Frames
messungenRuckenlageExp1 = ruckenlage * patienten * frames
messungenSeitenlageExp1 = seitenlage * patienten * frames
messungenGesamtExp1 = messungenSeitenlageExp1 + messungenRuckenlageExp1

ruckenlage2 = 17 #Positionen in Rückenlage
seitenlage2 = 12
patienten2 = 8 #Anzahl der Patienten
frames2 = 20
messungenRuckenlageExp2 = ruckenlage2 * patienten2 * frames2
messungenSeitenlageExp2 = seitenlage2 * patienten2 * frames2
messungenGesamtExp2 = messungenSeitenlageExp2 + messungenRuckenlageExp2

ruckenlageGesamt = messungenRuckenlageExp1 + messungenRuckenlageExp2
print("\nAufgabe B: Wie viele Messungen in Rückenlage?")
print("Es wurden " + str(messungenRuckenlageExp1) + " Werte gemessen in Rückenlage für Experiment 1.")
print("Es wurden " + str(messungenRuckenlageExp2) + " Werte gemessen in Rückenlage für Experiment 2.")
print("Somit sind es ingesamt " + str(ruckenlageGesamt) + "Messungen für die auf dem Rücken liegende Postition.")


#hier Prozentsatz für Experiment 1 mit Druckpunkt über 200 17 Mattendaten auf 13 Personen
#Aufgabe C: Den Durchschnitt errechnen für Experiment 1 und 2, welchen Prozentsatz
#der Mattenoberfläche einen Druckwert über 200(Experiment1) und über 100 (Experiment 2)haben:
# C1 in Rückenlageposition
# C2 in Seitenlageposition
# C3 wenn die obere und untere Mattenhälfte getrennt betrachtet werden
# a) Bettneigung von 0 Grad
# b) Bettneidung von 60 Grad
prozentExp1 = (prozentsatzGesamtSeitenlageX + prozentsatzGesamtRuckenlageX) / (patienten)
prozentExp1Ruckenlage = prozentsatzGesamtRuckenlageX / patienten
prozentExp1Seitenlage = prozentsatzGesamtSeitenlageX / patienten
print("\nAufgabe C für Experiment 1:")
print("Aufgabe C1: Druckwerte über 200 in Rückenlage für Experiment 1:")
print("Prozentsatz über 200 für Experiment 1 in Rückenlage ist: ", prozentExp1Ruckenlage)

print("\nAufgabe C2: Druckwerte über 200 in Seitenlage für Experiment 1:")
print("Prozentsatz über 200 für Experiment 1 in Seitenlage ist: ", prozentExp1Seitenlage)

print("\nAufgabe C3: Druckwerte über 200 obere und untere Mattenhälfte getrennt betrachtet:")
print("Aufgabe C3 a): Bettneigung von 0 Grad")
obereFinalNull = obereGesamtNull / patienten
untereFinalNull = untereGesamtNull /patienten
obereFinal60 = obereGesamt60 / patienten
untereFinal60 = untereGesamt60 / patienten

obereFinalNullLeftRight = obereGesamtNullLeftRight / patienten
untereFinalNullLeftRight = untereGesamtNullLeftRight /patienten

#print("Obere Mattenhälfte über 200 im Durchschnitt bei Neigung 0 in Rückenlage: ", obereFinalNull)
#print("Untere Mattenhälfte über 200 im Durchschnitt bei Neigung 0 in Rückenlage: ", untereFinalNull)
#obere Mattenhalfte geteilt durch die untere Mattenhaelfte
neigungNullsupine = obereFinalNull / untereFinalNull
neigung60supine = obereFinal60 / untereFinal60

neigungNullLeftRight = obereFinalNullLeftRight / untereFinalNullLeftRight
print("\nObere Mattenhälfte geteilt durch die untere Mattenhälfte für Neigung NUll Grad \n"
      "in Rückenlage bei Experiment 1 ergibt einen Prozentsatz von: ", neigungNullsupine)
print("\nObere Mattenhälfte geteilt durch die untere Mattenhälfte für Neigung NUll Grad \n"
      "in Seitenlage bei Experiment 1 ergibt einen Prozentsatz von: ", neigungNullLeftRight)
print("\nAufgabe C3 b): Bettneigung von 60 Grad")
#print("Obere Mattenhälfte über 200 im Durchschnitt bei Neigung 60 in Rückenlage: ", obereFinal60)
#print("Untere Mattenhälfte über 200 im Durchschnitt bei Neigung 60 in Rückenlage: ", untereFinal60)
print("Obere Mattenhälfte geteilt durch die untere Mattenhälfte für Neigung 60 Grad \n"
      "bei Experiment 1 ergibt einen Prozentsatz von: ", neigung60supine)


#hier Prozentsatz für Experiment 2 mit Druckpunkt über 200
prozentsatzGesamt = 0
prozentsatzGesamtRuckenlage = 0
prozentsatzGesamtSeitenlage = 0
prozentsatzGesamtRuckenlageX = 0
prozentsatzGesamtSeitenlageX = 0
prozentsatzGesamtX = 0
prozentsatzSeitenlage = 0
prozentsatzRuckenlage = 0

obereNeigungNull = 0
untereNeigungNull = 0
obereNeigung60 = 0
untereNeigung60 = 0

untereGesamtNull = 0
obereGesamtNull = 0
untereGesamt60 = 0
obereGesamt60 = 0

supineNeigungNull = 0
supineNeigung60 = 0

leftRightNull = 0
leftRight60 = 0

supineNeigungNullobere = 0
supineNeigung60obere = 0
supineNeigungNulluntere = 0
supineNeigung60untere = 0

leftRightNullobere = 0
leftRight60obere = 0
leftRightNulluntere = 0
leftRight60untere = 0

obereNeigungNullLeftRight =0
untereNeigungNullLeftRight = 0

untereGesamtNullLeftRight = 0
obereGesamtNullLeftRight = 0

abc = ""
number = 1
j = 1
z = 1
while j < 9:
    if z == 1:
        wort = "Air_Mat"
        wort2 = "Matrix_Air_"
    else:
        wort = "Sponge_Mat"
        wort2 = "Matrix_Sponge_"
    i = 1
    ii = 1
    iii = 1
    iv = 1
    v = 1
    while i < 30:
        if i < 11:
            abc = "B"
            number = i
            #print("jetzt in B und i ist ", i)
        elif i > 10 and i < 14:
            abc = "C"
            number = ii
            ii += 1
            #print("jetzt in C und i ist ", i)
        elif i > 13 and i < 17:
            abc = "D"
            number = iii
            iii+= 1
            #print("jetzt in D und i ist ", i)
        elif i > 16 and i < 23:
            abc = "E"
            number = iv
            iv += 1
            #print("jetzt in E und i ist ", i)
        elif i > 22 and i < 30:
            abc = "F"
            number = v
            v += 1
            #print("jetzt in F und i ist ", i)
        pfad = sys.argv[3] + str(j) + "/"+ wort + "/" + wort2 + abc
        #pfad = "C:\\Users\\adidr\\Desktop\\UNI\\Digital Health\\a-pressure-map-dataset-for-in-bed-posture-classification-1.0.0\\experiment-ii\\S1\\"+ wort + "\\" + wort2 + abc
        string = pfad + str(number) + '.txt'
        datei2 = open(string,'r')
        #print(datei2.read())
        count = 0
        liste = []
        neuListe = []
        for zeile in datei2:

            space = 0
            t = zeile.rsplit(" ")
            t = zeile.rstrip()
            #print(t)
            neuListe.append(t)

            """for x in zeile:
                if x == '\n':
                    count += 1
                if x == '\t':
                    space += 1
                if x != '\n' and x != '\t':
                    liste.append(int(x))"""
        #print(neuListe)
        finalListe = []
        for x in neuListe:
            #print(x)
            #print(x)
            p = x.split()
            #finalListe = finalListe + int(x)
            #for f in range(0, len(p)):
            finalListe.append(p)

        neuListe = []
        for o in finalListe:
            neuListe = neuListe + o

        finalListe = neuListe
        #print(finalListe)
        counter = 0
        counterNichtNull = 0
        for x in finalListe:
            if x != '\n':
                counter += 1
            if x != '0':
                counterNichtNull += 1
        #print(finalListe)
        #hier Aufgabe B: Wie viele Messungen in Rückenlage
        anzahlNullen = counter - counterNichtNull
        haelfte = counter // 2
        viertel = haelfte // 2
        dreiviertel = counter * 0.7
        #print(finalListe)
        # hier aufgabe C: durchschnittlicher Prozentsatz der Matte über 200
        bigger200 = 0
        for x in finalListe:
            if int(x) >= 100:
                bigger200 += 1
        #Aufgabe C1
        #Rückenlage messen
        if abc =="B" or abc == "F":
            prozentsatzRuckenlage = (bigger200 / counter) * 100
            #print("Prozentsatz von Matte " + str(i) + " in Rückenlage: " + str(prozentsatzRuckenlage))
        #Aufgabe C2
        #Seitenlage messen
        if abc == "C" or abc == "D" or abc == "E":
            prozentsatzSeitenlage = (bigger200 / counter) * 100
            #print("Prozentsatz von Matte " + str(i) + " in Seitenlage: " + str(prozentsatzSeitenlage))

        #Aufgabe C3 obere und untere Mattenhälfte
        obere = 0
        untere = 0
        lauf = 0
        for x in finalListe:
            lauf += 1
            if x != '\n' and lauf < haelfte:
                if x != '0':
                    if int(x) > 100:
                        obere += 1
            if x != '\n' and lauf > haelfte and lauf < counter:
                if x != '0':
                    if int(x) > 100:
                        untere += 1
        if abc != "F" or v > 1:
            prozentsatzObere = (obere/counter) * 100
            prozentsatzUntere = (untere/counter) * 100
            obereNeigungNull += prozentsatzObere
            untereNeigungNull += prozentsatzUntere

        if abc == "F" and v == 7:
            prozentsatzObere = (obere / haelfte) * 100
            prozentsatzUntere = (untere / haelfte) * 100
            obereNeigung60 += prozentsatzObere
            untereNeigung60 += prozentsatzUntere

        #supine bed inclination 0
        if abc == "B" or (abc == "F" and v == 1):
            supineNeigungNullobere = (obere/ haelfte) * 100
            supineNeigungNulluntere = (untere / haelfte) * 100
            obereNeigungNull += supineNeigungNullobere
            untereNeigungNull += supineNeigungNulluntere
        #supine bed inclination 60
        if abc != "B" or (abc == "F" and v == 7):
            supineNeigung60obere = (obere / haelfte) * 100
            supineNeigung60untere = (untere / haelfte) * 100
            obereNeigung60 += supineNeigung60obere
            untereNeigung60 += supineNeigung60untere
        #left/right bed inclination 0
        if abc != "B" and abc != "F":
            leftRightNullobere = (obere / haelfte) * 100
            leftRightNulluntere = (untere / haelfte) * 100
            obereNeigungNullLeftRight += leftRightNullobere
            untereNeigungNullLeftRight += leftRightNulluntere

        if i == 1 or i > 7 and i < 18:
            prozentsatzGesamtRuckenlage += prozentsatzRuckenlage
        #print("Prozent Rücken: ", prozentsatzGesamtRuckenlage)
        if i > 1 and i < 8:
            prozentsatzGesamtSeitenlage += prozentsatzSeitenlage
        i = i + 1
    prozentsatzGesamtRuckenlage = prozentsatzGesamtRuckenlage / 9
    prozentsatzGesamtSeitenlage = prozentsatzGesamtSeitenlage / 8
    prozentsatzGesamtRuckenlageX += prozentsatzGesamtRuckenlage
    prozentsatzGesamtSeitenlageX += prozentsatzGesamtSeitenlage

    #supine position bed inclination 0
    untereNeigungNull = untereNeigungNull / 11
    untereGesamtNull += untereNeigungNull
    obereNeigungNull = obereNeigungNull / 11
    obereGesamtNull += obereNeigungNull
    #supine position bed inclination 60
    untereNeigung60 = untereNeigung60
    untereGesamt60 += untereNeigung60
    obereNeigung60 = obereNeigung60
    obereGesamt60 += obereNeigung60

    #left/right position bed inclination 0
    untereNeigungNullLeftRight = untereNeigungNullLeftRight / 12 # geteilt durch die Anzahl der Positionen
    untereGesamtNullLeftRight += untereNeigungNullLeftRight
    obereNeigungNullLeftRight = obereNeigungNullLeftRight / 12 #geteilt durch die Anzahl der Positionen
    obereGesamtNullLeftRight += obereNeigungNullLeftRight
    if z == 1:
        z = 2
    else:
        j = j + 1

prozentExp2Ruckenlage = prozentsatzGesamtRuckenlageX / patienten2
prozentExp2Seitenlage = prozentsatzGesamtSeitenlageX / patienten2

print("\nAufgabe C für Experiment 2:")
print("Aufgabe C1: Druckwerte über 100 in Rückenlage für Experiment 2:")
print("Prozentsatz über 100 für Experiment 2 in Rückenlage ist: ", prozentExp2Ruckenlage)

print("\nAufgabe C2: Druckwerte über 100 in Seitenlage für Experiment 2:")
print("Prozentsatz über 200 für Experiment 2 in Seitenlage ist: ", prozentExp2Seitenlage)

print("\nAufgabe C3: Druckwerte über 100 obere und untere Mattenhälfte getrennt betrachtet:")
print("Aufgabe C3 a): Bettneigung von 0 Grad")
obereFinalNull = obereGesamtNull / patienten2
untereFinalNull = untereGesamtNull /patienten2
obereFinal60 = obereGesamt60 / patienten2
untereFinal60 = untereGesamt60 / patienten2

obereFinalNullLeftRight = obereGesamtNullLeftRight / patienten2
untereFinalNullLeftRight = untereGesamtNullLeftRight /patienten2
#print("Obere Mattenhälfte über 100 im Durchschnitt bei Neigung 0: ", obereFinalNull)
#print("Untere Mattenhälfte über 100 im Durchschnitt bei Neigung 0: ", untereFinalNull)
neigungNullsupine = obereFinalNull / untereFinalNull
neigung60supine = obereFinal60 / untereFinal60
neigungNullLeftRight = obereFinalNullLeftRight / untereFinalNullLeftRight
print("\nObere Mattenhälfte geteilt durch die untere Mattenhälfte \n"
      "für Neigung Null Grad in Rückenlage bei Experiment 2 ergibt einen Prozentsatz von: ", neigungNullsupine)
print("\nObere Mattenhälfte geteilt durch die untere Mattenhälfte \n"
      "für Neigung Null Grad in Seitenlage bei Experiment 2 ergibt einen Prozentsatz von: ", neigungNullLeftRight)

print("\nAufgabe C3 b): Bettneigung von 60 Grad")
#print("Obere Mattenhälfte über 100 im Durchschnitt bei Neigung 60: ", obereFinal60)
#print("Untere Mattenhälfte über 100 im Durchschnitt bei Neigung 60: ", untereFinal60)

print("\nObere Mattenhälfte geteilt durch die untere Mattenhälfte für Neigung 60 Grad \n"
      "in Rückenlage bei Experiment 2 ergibt einen Prozentsatz von: ", neigung60supine)

print("\nAufgabe D: Hat eine Normalisierung stattgefunden anhand der Patientendaten?")
print("Es hat keine Normalisierung stattgefunden, da die Patientendaten keinen Merkmale \n"
      "von zusätzlichen Attributen vorweisen und das einfügen von Attributen, die Ergebnisse nicht verändern.")

print("\nAufgabe E: Berücksichtig auf C1, ist ein Zusammenhang erkennbar zwischen der Körpergröße \n"
      "des Patienten und den gefundenen Mattenpunkten in Rückenlage")
print("Die Position in Rückenlage nimmt einen Großteil der Matte ein und trifft somit eine größere Anzahl der Druckwerte.\n"
      "Aus diesem Grund ist die Anzahl der getroffenen Punkte abhängig von der Körpergröße.\n"
      "Je größer der Patient, desto größer die Anzahl der getroffenen Druckpunkte.")


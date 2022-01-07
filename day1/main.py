# Das ist ein Kommentar Kommentar

# woche 1: operatoren
# woche 2: elementare datentypen
# woche 3: variablen
# woche 4: bedingungen (if else)
# woche 5: funktionen
# woche 6: schleifen

zaehler = 0
liste = []

datei = open('input.txt')

# automatisch jede zeile der datei lesen, umwandeln und in die liste speichern

# datei besteht aus zeilen, mache etwas für jede zeile
for zeile in datei:
    liste.append(int(zeile))

# liste ist gefüllt mit allen Zahlen, die verglichen werden sollen

# iteriere ueber jedes element der liste (bis auf das letzte!)
# vergleiche aktuelle zahl mit der naechsten zahl in der liste
for i in range(len(liste) - 1):
    # falls aktuelle zahl der liste kleiner als naechste zahl der liste ...
    if (liste[i] < liste[i + 1]): # liste[i] < liste[i + 1] ist entweder wahr oder falsch
        # erhoeher zaehler
        zaehler = zaehler + 1
print('part1:', zaehler)

zaehler = 0

for i in range(len(liste) - 3):
    erste_summe    = liste[i] + liste[i + 1] + liste[i + 2]
    naechste_summe = liste[i + 1] + liste[i + 2] + liste[i + 3]

    if erste_summe < naechste_summe:
        zaehler = zaehler + 1

print('part2:', zaehler)

# zaehler enthaelt den gesuchten wert
#print(zaehler)

datei = open('input.txt')

horizontal = 0
depth = 0

for zeile in datei:

    # zeile.strip().split(' ') liefert z.B. ['forward', 5]
    # wir weisen der var 'befehl' das erste listenelement zu
    # wir weisen der var 'zaehler' das zweite listenelement zu'

    befehl, zaehler = zeile.strip().split(' ')
    # zaeler muss noch als 'zahl' (integer) interpretiert werden
    zaehler = int(zaehler) 
    # eigentliche Implementierung der Aufgabe
    # pruefe den befehl

    """
    forward X increases the horizontal position by X units.
    down X increases the depth by X units.
    up X decreases the depth by X units.
    """

    if befehl == 'forward':
        horizontal = horizontal + zaehler
    
    if befehl == 'down':
        depth = depth + zaehler

    if befehl == 'up':
        depth = depth - zaehler

print('part One:', horizontal*depth)


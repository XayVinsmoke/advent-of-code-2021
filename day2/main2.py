datei = open('input.txt')

horizontal = 0
depth = 0
aim = 0

for zeile in datei: befehl, zaehler = zeile.strip().split(' ')
    zaehler = int(zaehler) 

    if befehl == 'forward':
        horizontal = horizontal + zaehler
        depth      = depth + aim * zaehler

    if befehl == 'down':
        aim = aim + zaehler

    if befehl == 'up':
        aim = aim - zaehler

print('part Two:', horizontal*depth)

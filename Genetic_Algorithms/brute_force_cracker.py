'''

Safe knacken durch Brute-Force Methode.
Dauert sehr lange, da alle Kombinationen durchprobiert werden

'''



import time
from itertools import product

# Startzeit
start_time = time.time()

# Schlosskombination
combo = (9, 9, 7, 6, 5, 4, 3, 6, 2)

# Wir benutzen die Funktion product von itertools
# 0-9 mögliche Zahlen zum probieren
for perm in product([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], repeat=len(combo)):
    if perm == combo:
        print(f"Cracked! {combo}{perm}")

# Endzeit. Um Dauer des Programs zu berechnen
end_time = time.time()

print(f"\nRuntime for this program was {end_time - start_time} seconds.")
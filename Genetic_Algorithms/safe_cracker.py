"""

Optimierter Safe Knacker, druch stufenweises annähern.
'Hill Climbing algorithm'

"""
import time
from random import randint, randrange

def fitness(combo, attempt):
    """
    Ziffern von echter Kombination mit Annäherung vergleichen
    +1, wenn 2 Stellen übereinstimmen

    """
    grade = 0
    for i, j in zip(combo, attempt):
        if i == j:
            grade += 1
    return grade

def main():
    """Schlosskombination als String eingeben und Algorithmus laufen lassen"""
    combination = '6822858902'
    print(f"Combination = {combination}")
    # Umwandeln in eine Liste
    combo = [int(i) for i in combination]

    # Anfangen random an Stellen zu raten und mit Original vergleichen
    best_attempt = [0] * len(combo)
    best_attempt_grade = fitness(combo, best_attempt)

    count = 0

    # Anfangen zu raten
    while best_attempt != combo:

        next_try = best_attempt[:]
        # zufällig Stelle und Wert finden
        lock_wheel = randrange(0, len(combo))
        next_try[lock_wheel] = randint(0, 9)

        # Bewerten, ob es näher an Original ist
        next_try_grade = fitness(combo, next_try)
        if next_try_grade > best_attempt_grade:
            best_attempt = next_try[:]
            best_attempt_grade = next_try_grade
        print(next_try, best_attempt)
        count += 1

    print()
    print(f"Cracked! {best_attempt}", end=' ')
    print(f"in {count} tries!")

if __name__ == '__main__':    
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print("\nRuntime for this program was {:.5f} seconds.".format(duration))            

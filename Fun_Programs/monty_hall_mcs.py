'''

Monty Hall Problem lösen, mithilfe von Monte-Carlo-Simulation

'''

import random


def user_prompt(prompt, default=None):
    """Erstellt Anweisung und Anzahl an Wiederholungen"""
    prompt = f"{prompt}[{default}]: "
    response = input(prompt)
    if not response and default:
        return default
    else:
        return response

# Anweisung und Anzahl an Wiederholungen initialisieren
# Keine Eingabe bedeutet 20000 Wiederholungen
num_runs = int(user_prompt("Input number of runs", "20000"))

# Zähler erstellen
first_choice_wins = 0
pick_change_wins = 0
doors = ['a', 'b', 'c']

# Monte Carlo
for i in range(num_runs):
    winner = random.choice(doors)
    pick = random.choice(doors)

    if pick == winner:
        first_choice_wins += 1
    else:
        pick_change_wins += 1
print(f"Wins with original pick = {first_choice_wins}.")
print(f"Wins with changed pick = {pick_change_wins}.")
print("Probability of winning with initial guess: {:.2f}"
      .format(first_choice_wins/num_runs))
print("Probability of winning with changed guess: {:.2f}"
      .format(pick_change_wins/num_runs))

input("\nPress Enter key to exit.")
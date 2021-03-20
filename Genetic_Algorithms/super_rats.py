'''

Durch Genetic Algorithms möglichst grosse Ratten züchten

'''


import time
import random
import statistics

GOAL = 50_000
NUM_RATS = 20
INITIAL_MIN_WT = 200
INITIAL_MAX_WT = 600
INITIAL_MODE_WT = 300
MUTATE_ODDS = 0.01
MUTATE_MIN = 0.5
MUTATE_MAX = 1.2
LITTER_SIZE = 8
LITTERS_PER_YEAR = 10
GENERATION_LIMIT = 500

# Gerade Anazhl an Ratten für Paarbildung
if NUM_RATS % 2 != 0:
    NUM_RATS += 1

def populate(num_rats, min_wt, max_wt, mode_wt):
    """Anfangspopulation erzeugen"""
    return [int(random.triangular(min_wt, max_wt, mode_wt))\
            for i in range(num_rats)]

def fitness(population, goal):
    """Durchschnittswert mit GOAL vergleichen"""
    ave = statistics.mean(population)
    return ave / goal

def select(population, to_retain):
    """Population verkleiner und nach Geschlecht sortieren. Männchen immer grösser als Weibchen"""
    sorted_population = sorted(population)
    to_retain_by_sex = to_retain//2
    members_per_sex = len(sorted_population)//2
    females = sorted_population[:members_per_sex]
    males = sorted_population[members_per_sex:]
    selected_females = females[-to_retain_by_sex:]
    selected_males = males[-to_retain_by_sex:]
    return selected_males, selected_females

def breed(males, females, litter_size):
    """Männchen und Weibchen random paaren um Nachwuchs zu erzeugen"""
    random.shuffle(males)
    random.shuffle(females)
    children = []
    for male, female in zip(males, females):
        for child in range(litter_size):
            child = random.randint(female, male)
            children.append(child)
    return children
def mutate(children, mutate_odds, mutate_min, mutate_max):
    """Zufällige Mutationen erzeugen in Nachwuchs"""
    for index, rat in enumerate(children):
        if mutate_odds >= random.random():
            children[index] = round(rat * random.uniform(mutate_min, mutate_max))

    return children

def main():
    """Anfangspopulation generieren und durchschleifen bis Fitness > 1 wird"""
    generations = 0
    parents = populate(NUM_RATS, INITIAL_MIN_WT, INITIAL_MAX_WT,
                       INITIAL_MODE_WT)
    print(f"Initial population weights = {parents}")
    popl_fitness = fitness(parents, GOAL)
    print(f"Initial population fitness = {popl_fitness}")
    print(f"Number to retain = {NUM_RATS}")

    ave_wt = []

    while popl_fitness < 1 and generations < GENERATION_LIMIT:
        selected_males, selected_females = select(parents, NUM_RATS)
        children = breed(selected_males, selected_females, LITTER_SIZE)
        children = mutate(children, MUTATE_ODDS, MUTATE_MIN, MUTATE_MAX)
        parents = selected_males + selected_females + children
        popl_fitness  = fitness(parents, GOAL)
        print(f"Generation {generations} = {popl_fitness}")
        ave_wt.append(int(statistics.mean(parents)))
        generations += 1
    print(f"Average weight per generation = {ave_wt}")
    print(f"\nNumber of generations = {generations}")
    print(f"Number of years = {generations/LITTERS_PER_YEAR}")

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print(f"\nRuntime for this program was {duration} seconds.")
"""

.txt Wörterbuch einlesen und als Liste wiedergeben

"""

from termcolor import colored

def load(file):
    # Datei einlesen und in Kleinbuchstaben abspeichern
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt

    except IOError:
        print("IOError! Terminating program!", colored('Error', 'red'))

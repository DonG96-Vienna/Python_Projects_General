'''

Sieb des Eratosthenes um Primzahlen zu finden von 1 bis n

'''

n = input("Enter an end number: ")

# n muss zu einem integer gemacht werden
n = int(n)

# Liste von 1 bis n erstellen (Unser Sieb)
num_list = [x for x in range(2, n+1)]

# Funktionsweise des Sieb von Eratosthenes
for i in num_list:
    for j in range(2, n+1):
        num = j*i
        if num <= n and num in num_list:
            num_list.remove(num)


for prime in num_list:
    print(f"The number {prime} is a prime number!")
'''

Bekanntes Collatz-Conjecture

'''

import matplotlib.pyplot as plt

num = int(input("Enter a starting number larger than 0: "))

lst = [num]

while num != 1:

    if num % 2 == 0:
        num = num // 2

    else:
        num = 3*num +1

    lst.append(num)

# Entwicklung der Collatz-Zahlen veranschaulichen. Geht am Ende gegen y = 1
plt.plot(lst)
plt.ylabel('Collatz number progression')
plt.xlabel('number of iterations')
plt.axhline(y=1, color='r', linestyle='-')
plt.show()
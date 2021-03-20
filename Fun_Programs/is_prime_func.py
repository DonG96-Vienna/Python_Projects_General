'''

Berechnet ob eine Zahl eine Primzahl ist

'''


def is_prime(num):

    for i in range(2, num//2 + 1):
        if num % i == 0:
            print(f"{num} is not prime!")
            return 0



    print(f"{num} is prime!")


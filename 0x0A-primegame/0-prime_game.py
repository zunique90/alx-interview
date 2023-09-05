#!/usr/bin/python3
"""Prime Game"""


def getPrimeNumbers(num):
    """returns list of prime numbers from 1 to num"""
    primeNumbers = []
    filtered = [True] * (num + 1)
    for prime in range(2, num + 1):
        if (filtered[prime]):
            primeNumbers.append(prime)
            for i in range(prime, num + 1, prime):
                filtered[i] = False
    return primeNumbers


def isWinner(x, nums):
    """Determines the winner of Prime Game"""

    if x is None or nums is None or x == 0 or nums == []:
        return None

    maria_wins = 0
    ben_wins = 0

    for i in range(x):
        if len(getPrimeNumbers(nums[i])) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None

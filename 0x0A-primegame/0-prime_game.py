#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Determines the winner of each game"""

    def isPrime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def getPrimeCount(num):
        count = 0
        for i in range(2, num + 1):
            if isPrime(i):
                count += 1
        return count

    if x is None or nums is None or x == 0 or nums == []:
        return None

    maria_wins = 0
    ben_wins = 0

    for num in nums:
        primeCount = getPrimeCount(num)
        if primeCount % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

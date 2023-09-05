def isWinner(x, nums):
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def canWin(num):
        if num == 1:
            return False
        if num == 2 or num % 2 == 1:
            return True
        return False

    maria_wins = 0
    ben_wins = 0

    for num in nums:
        if canWin(num):
            if isPrime(num):
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

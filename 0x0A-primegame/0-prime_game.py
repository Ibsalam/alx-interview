#!/usr/bin/python3
"""Prime game module.
"""

def sieve(n):
    """ Returns a list of prime numbers up to n using the Sieve of Eratosthenes. """
    primes = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if primes[p] == True:
            # Marking multiples of p as False
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]

def play_game(n):
    """ Simulates the game for a given n, returns 1 if Maria wins, 0 if Ben wins """
    if n < 2:
        return 0  # Ben wins if there are no primes for Maria to start with

    primes = sieve(n)
    prime_set = set(primes)

    turn = 0  # 0 for Maria, 1 for Ben
    while prime_set:
        # Pick the smallest prime and remove its multiples
        prime = min(prime_set)
        multiples = set(range(prime, n + 1, prime))
        prime_set -= multiples
        turn ^= 1  # Switch turns

    # The player who cannot make a move loses, so if turn == 1, Maria wins, else Ben wins
    return 1 if turn == 1 else 0

def isWinner(x, nums):
    """ Determines the winner over x rounds. """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if play_game(n) == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

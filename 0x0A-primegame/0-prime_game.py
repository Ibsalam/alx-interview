#!/usr/bin/python3
"""Prime game module.
"""

def isWinner(rounds, numbers):
    """Determines the winner of a prime game session with `rounds` rounds.
    """
    if rounds < 1 or not numbers:
        return None

    maria_wins, ben_wins = 0, 0

    # Generate primes up to the maximum number in the numbers list
    max_num = max(numbers)
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

    for num in range(2, int(max_num ** 0.5) + 1):
        if is_prime[num]:
            for multiple in range(num * num, max_num + 1, num):
                is_prime[multiple] = False

    # Count prime numbers for each round and decide winner
    for num in numbers:
        prime_count = sum(is_prime[:num + 1])
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins == ben_wins:
        return None
    return 'Maria' if maria_wins > ben_wins else 'Ben'


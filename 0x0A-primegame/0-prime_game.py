#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Prime Game
    """
    def sieve_of_eratosthenes(max_num):
        """Sieve of Eratosthenes to find primes up to max_num"""
        is_prime = [True] * (max_num + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
        for i in range(2, int(max_num**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, max_num + 1, i):
                    is_prime[j] = False
        return is_prime

    # Edge case: if no rounds are played
    if x == 0:
        return None

    # Get the maximum number in nums to compute primes up to that limit
    max_n = max(nums)
    primes_up_to_n = sieve_of_eratosthenes(max_n)

    # Maria and Ben's win counters
    maria_wins = 0
    ben_wins = 0

    # Play each round
    for n in nums:
        prime_count = sum(primes_up_to_n[2:n+1])
        if prime_count % 2 == 1:
            maria_wins += 1  # Maria wins if there is an odd number of primes
        else:
            ben_wins += 1  # Ben wins if there is an even number of primes
    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

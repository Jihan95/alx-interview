#!/usr/bin/python3
"""
make change
"""

def makeChange(coins, total):
    """
    make change
    """
    # If total is 0 or less, no coins are needed
    if total <= 0:
        return 0

    # Initialize the dp array where dp[i] is the minimum number of coins to make amount i
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins are needed to make 0

    # Process each coin and update dp array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, we cannot form the amount
    return dp[total] if dp[total] != float('inf') else -1

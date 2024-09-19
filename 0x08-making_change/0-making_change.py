def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize the DP array to a large number (representing infinity)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to reach a total of 0

    # Fill the DP array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means we cannot form the total
    return dp[total] if dp[total] != float('inf') else -1

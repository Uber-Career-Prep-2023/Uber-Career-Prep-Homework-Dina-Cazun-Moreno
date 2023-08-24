def coinChange(coins, target):
    dp = [0] * (target + 1)
    dp[0] = 1  # There's one way to make change for a target sum of 0 (using no coins)

    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]

    return dp[target]

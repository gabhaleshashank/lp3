# 0/1 Knapsack Problem using Dynamic Programming

def knapsack(values, weights, capacity):
    n = len(values)
    
    #create DP table (n+1) x (capacity+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    #build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]],
                               dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    #traceback to find selected items
    selected_items = []
    res = dp[n][capacity]
    w = capacity

    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == dp[i - 1][w]:
            continue
        else:
            selected_items.append(i)
            res -= values[i - 1]
            w -= weights[i - 1]

    selected_items.reverse()

    print("\nSelected items (by item number):", selected_items)
    return dp[n][capacity]

# ---- Main Code ----
if __name__ == "__main__":
    n = int(input("Enter number of items: "))
    values = list(map(int, input("Enter values of items (space separated): ").split()))
    weights = list(map(int, input("Enter weights of items (space separated): ").split()))
    capacity = int(input("Enter maximum capacity of knapsack: "))

    max_value = knapsack(values, weights, capacity)
    print(f"\nMaximum total value that can be carried: {max_value}")
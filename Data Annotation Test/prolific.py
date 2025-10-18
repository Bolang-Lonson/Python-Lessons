def maxCardCount(n, card):
    # Memoization table to store results of subproblems
    memo = {}

    def dp(i, sum):
        # Base case: if we've processed all cards
        if i == n:
            return 0

        # Check if the result is already computed
        if (i, sum) in memo:
            return memo[(i, sum)]

        # Option 1: Skip the current card
        skip = dp(i + 1, sum)

        # Option 2: Pick the current card if sum + card[i] >= 0
        pick = 0
        if sum + card[i] >= 0:
            pick = 1 + dp(i + 1, sum + card[i])

        # Store the result in the memoization table
        memo[(i, sum)] = max(skip, pick)
        return memo[(i, sum)]

    # Start the recursion with the first card and initial sum of 0
    return dp(0, 0)


# Read input values
n = int(input())
cards = list(map(int, input().split()))

# Find the maximum number of cards that can be picked up
result = maxCardCount(n, cards)

# Print the result
print(result)

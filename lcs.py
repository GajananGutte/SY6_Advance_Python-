"""
Write a program to find the longest common subsequence between two sequences.
"""
"""

def LCS(X, Y):
    m = len(X)
    n = len(Y)

    # Create DP table with (m+1) rows and (n+1) columns
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            # If characters are same
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            # If characters are different
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Length of LCS
    index = dp[m][n]

    # Create list to store LCS characters
    lcs = [""] * index

    # Start from bottom-right of DP table
    i = m
    j = n

    # Backtracking to find the actual LCS
    while i > 0 and j > 0:

        if X[i - 1] == Y[j - 1]:
            lcs[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1

        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1

        else:
            j -= 1

    return "".join(lcs)


# Main program
if __name__ == "__main__":

    X = "AGGTAB"
    Y = "GXTXAYB"

    result = LCS(X, Y)

    print("=" * 45)
    print("       LONGEST COMMON SUBSEQUENCE (LCS)")
    print("=" * 45)

    print("Sequence 1 (X) :", X)
    print("Sequence 2 (Y) :", Y)

    print("-" * 45)

    print("Longest Common Subsequence :", result)
    print("Length of LCS              :", len(result))

    print("=" * 45)
"""

=============================================
       LONGEST COMMON SUBSEQUENCE (LCS)
=============================================
Sequence 1 (X) : AGGTAB
Sequence 2 (Y) : GXTXAYB
---------------------------------------------
Longest Common Subsequence : GTAB
Length of LCS              : 4
=============================================

def lcs_recursive(seq1, seq2, idx1=0, idx2=0):
    if idx1 == len(seq1) or idx2 == len(seq2):
        return 0
    elif seq1[idx1] == seq2[idx2]:
        return 1 + lcs_recursive(seq1, seq2, idx1 + 1, idx2 + 1)
    else:
        option1 = lcs_recursive(seq1, seq2, idx1 + 1, idx2)
        option2 = lcs_recursive(seq1, seq2, idx1, idx2 + 1)
        return max(option1, option2)


# print(lcs_recursive("serendipitous", "precipitation"))
# print(lcs_recursive([1, 3, 5, 6, 7, 2, 5, 2, 3], [6, 2, 4, 7, 1, 5, 6, 2, 3]))


def lcs_memo(seq1, seq2):
    memo = {}

    def recurse(idx1=0, idx2=0):
        key = (idx1, idx2)

        if key in memo:
            return memo[key]
        elif idx1 == len(seq1) or idx2 == len(seq2):
            memo[key] = 0
        elif seq1[idx1] == seq2[idx2]:
            memo[key] = 1 + recurse(idx1 + 1, idx2 + 1)
        else:
            memo[key] = max(recurse(idx1 + 1, idx2), recurse(idx1, idx2 + 1))
        return memo[key]

    return recurse(0, 0)


# print(lcs_memo("serendipitous", "precipitation"))


def lcs_dp(seq1, seq2):
    n1, n2 = len(seq1), len(seq2)
    table = [[0 for x in range(n2 + 1)] for x in range(n1 + 1)]
    for idx1 in range(n1):
        for idx2 in range(n2):
            if seq1[idx1] == seq2[idx2]:
                table[idx1 + 1][idx2 + 1] = 1 + table[idx1][idx2]
            else:
                table[idx1 + 1][idx2 + 1] = max(
                    table[idx1][idx2 + 1], table[idx1 + 1][idx2]
                )
    # print(table)
    return table[-1][-1]


# print(lcs_dp("serendipitous", "precipitation"))


def max_profit_recursive(weights, profits, capacity, idx=0):
    if idx == len(weights):
        return 0
    elif weights[idx] > capacity:
        return max_profit_recursive(weights, profits, capacity, idx + 1)
    else:
        option1 = max_profit_recursive(weights, profits, capacity, idx + 1)
        option2 = profits[idx] + max_profit_recursive(
            weights, profits, capacity - weights[idx], idx + 1
        )
        return max(option1, option2)


# print(
#     max_profit_recursive(
#         weights=[4, 5, 6],
#         profits=[1, 2, 3],
#         capacity=15,
#     )
# )


def max_profit_memo(capacity, weights, profits):
    memo = {}

    def recurse(idx, remaining):
        key = (idx, remaining)
        if key in memo:
            return memo[key]
        elif idx == len(weights):
            memo[key] = 0
        elif weights[idx] > remaining:
            memo[key] = recurse(idx + 1, remaining)
        else:
            memo[key] = max(
                recurse(idx + 1, remaining),
                profits[idx] + recurse(idx + 1, remaining - weights[idx]),
            )
        return memo[key]

    return recurse(0, capacity)


# print(
#     max_profit_memo(
#         weights=[4, 5, 6],
#         profits=[1, 2, 3],
#         capacity=15,
#     )
# )


def max_profit_dp(weights, profits, capacity):
    n = len(weights)
    table = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for idx in range(n):
        for c in range(capacity + 1):
            if weights[idx] > c:
                table[idx + 1][c] = table[idx][c]
            else:
                table[idx + 1][c] = max(
                    table[idx][c], profits[idx] + table[idx][c - weights[idx]]
                )
    print(table)
    return table[-1][-1]


print(
    max_profit_dp(
        weights=[4, 5, 6],
        profits=[1, 2, 3],
        capacity=15,
    )
)

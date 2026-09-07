from collections import deque
from re import I

COUNT = 12

def main():
    total_joltage = 0
    with open("input.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            line = line.strip()
            digits = [int(d) for d in line]
            N = len(digits)

            dp = [[0] * COUNT for _ in range(N)]
            for i in range(N):
                dp[i][0] = digits[i]

            for p in range(1, COUNT):
                for i in range(N):
                    r = digits[i] * (10 ** p)
                    best = r
                    if p > 0:
                        for j in range(i + 1, N - p + 1):
                            best = max(best, r + dp[j][p - 1])
                    dp[i][p] = best

            total_joltage += max(dp[i][COUNT - 1] for i in range(N - COUNT + 1))

    
    print(total_joltage)

if __name__ == "__main__":
    main()
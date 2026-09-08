def main():
    grid = []
    with open("input.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            line = line.strip()
            grid.append([1 if c == "@" else 0 for c in line])
    
    D = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
    M, N = len(grid), len(grid[0])
    accessible_rolls = 0
    for m in range(M):
        for n in range(N):
            if grid[m][n] == 0:
                continue
            
            adjacent_rolls_count = 0
            for dx, dy in D:
                dx, dy = dx + n, dy + m
                if 0 <= dx < N and 0 <= dy < M and grid[dy][dx] == 1:
                    adjacent_rolls_count += 1
                    
            if adjacent_rolls_count < 4:
                accessible_rolls += 1

    print(accessible_rolls)

if __name__ == "__main__":
    main()
def main():
    dial = 50
    clicks_on_zero = 0
    with open("input.txt", "r", encoding="utf8") as f:
        for line in f:
            direction = 1 if line[0] == "R" else -1
            moves = int(line[1:])
            total = moves * direction
            if direction == 1:
                clicks_on_zero += (dial + total) // 100
            else:
                clicks_on_zero += ((100 - (dial if dial != 0 else 100)) + total * -1) // 100
            dial = (dial + total) % 100
    
    print(clicks_on_zero)

if __name__ == "__main__":
    main()
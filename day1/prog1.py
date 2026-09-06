


def main():
    dial = 50
    zero_pointing_amount = 0
    with open('input.txt', 'r', encoding='utf8') as f:
        for line in f:
            direction = (1 if line[0] == "R" else -1)
            moves = int(line[1:])
            dial = (dial + direction * moves) % 100
            if dial == 0:
                zero_pointing_amount += 1
    print(zero_pointing_amount)

if __name__ == "__main__":
    main()
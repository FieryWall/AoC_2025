def main():
    total_joltage = 0
    with open("input.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            best_left = 0
            best_index = 0
            for i in range(len(line) - 2):
                num = int(line[i])
                if num > best_left:
                    best_left = num
                    best_index = i

            best_right = 0
            for i in range(best_index + 1, len(line) - 1):
                num = int(line[i])
                if num > best_right:
                    best_right = num

            total_joltage += int(f"{best_left}{best_right}")
    
    print(total_joltage)

if __name__ == "__main__":
    main()
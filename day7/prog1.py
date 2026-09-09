def main():
    beams = set()
    splits = 0
    with open("input.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            for i, ch in enumerate(line):
                if ch == "S":
                    beams.add(i)
                if ch == "^" and i in beams:
                    beams.remove(i)
                    beams.add(i - 1)
                    beams.add(i + 1)
                    splits += 1

    print(splits)

if __name__ == "__main__":
    main()
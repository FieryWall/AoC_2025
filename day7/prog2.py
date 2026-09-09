def main():
    timelines = {}
    with open("input.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            for i, ch in enumerate(line):
                if ch == "S":
                    timelines[i] = 1
                if ch == "^" and i in timelines:
                    timelines[i - 1] = timelines.get(i - 1, 0) + timelines[i]
                    timelines[i + 1] = timelines.get(i + 1, 0) + timelines[i]
                    del timelines[i]

    print(sum(timelines.values()))

if __name__ == "__main__":
    main()
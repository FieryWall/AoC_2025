def main():
    all_invalids = set[int]()
    base = 1
    while base < 999999:
        repeats = 2
        num_str = ""
        while len(num_str) < 13:
            num_str = str(base) * repeats
            all_invalids.add(int(num_str))
            repeats += 2
        base += 1

    invalid_ids_sum = 0
    with open("input.txt", "r", encoding="utf8") as f:
        ranges = f.read().split(",")
        for r in ranges:
            edges = r.split("-")
            for num in range(int(edges[0]), int(edges[1]) + 1):
                if num in all_invalids:
                    invalid_ids_sum += num
    
    print(invalid_ids_sum)
        

if __name__ == "__main__":
    main()
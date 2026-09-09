from math import prod

def main():
    operands = None
    grand_total = 0
    with open("input.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            N = len(line)
            if line[0] == "*" or line[1] == "+":
                i = 0
                for operator in line.split(" "):
                    if not operator:
                        continue
                    
                    res = 1 if operator == "*" else 0
                    while i < N:
                        if operands[i].strip():
                            if operator == "*":
                                res *= int(operands[i])
                            else:
                                res += int(operands[i])
                            i += 1
                        else:
                            i += 1
                            break
                    
                    grand_total += res
                print(grand_total)
                return

            if not operands:
                operands = [""] * N

            for i, ch in enumerate[str](line):
                operands[i] += ch

if __name__ == "__main__":
    main()
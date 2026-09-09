from math import prod

def main():
    operands = None
    grand_total = 0
    with open("input.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            line = line.strip()
            if line[0] == "*" or line[1] == "+":
                i = 0
                for operator in line.split(" "):
                    if not operator:
                        continue
                    if operator == "*":
                        grand_total += prod(operands[i])
                    else:
                        grand_total += sum(operands[i])
                    i += 1
                print(grand_total)
                return

            line_operands = [int(op) for op in line.split(" ") if op]
            N = len(line_operands)
            if not operands:
                operands = [[] for _ in range(N)]

            for i in range(N):
                operands[i].append(line_operands[i])

if __name__ == "__main__":
    main()
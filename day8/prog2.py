import heapq
from math import prod, sqrt


X, Y, Z = 0, 1, 2

def main():
    junction_boxes = []
    uf = []
    with open("input.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            junction_boxes.append([int(v) for v in line.strip().split(",")])
            uf.append(len(uf))

    pairs = []
    for i, a in enumerate(junction_boxes):
        for j in range(i + 1, len(junction_boxes)):
            b = junction_boxes[j]
            dist = sqrt(abs(a[X] - b[X])**2 + abs(a[Y] - b[Y])**2 + abs(a[Z] - b[Z])**2)
            heapq.heappush(pairs, (dist, i, j))

    uv = [1] * len(uf)
    while True:
        _, i, j = heapq.heappop(pairs)
        g, r = i, j
        while uf[g] != g: g = uf[g]
        while uf[r] != r: r = uf[r]
        if g == r: continue
        uv[g] += uv[r]
        uv[r] = 0
        uf[r] = i
        if uv[g] == len(junction_boxes):
            print(junction_boxes[i][X] * junction_boxes[j][X])
            return

if __name__ == "__main__":
    main()
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
    for _ in range(1000):
        _, i, j = heapq.heappop(pairs)
        g = i
        while uf[g] != g: g = uf[g]
        while uf[j] != j: j = uf[j]
        if g == j: continue
        uv[g] += uv[j]
        uv[j] = 0
        uf[j] = i
    
    print(prod(sorted(uv, reverse=True)[:3]))

if __name__ == "__main__":
    main()
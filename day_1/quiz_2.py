from collections import Counter

left = []
right = Counter()

with open("input.txt", "r") as file:
    for line in file:
        l, r = line.split()
        left.append(int(l))
        right[int(r)] += 1

similarity_map = {}
total = 0

for num in left:
    if num not in similarity_map:
        count = right.get(num, 0)
        similarity_map[num] = count

    total += (num * similarity_map[num])

print(f"Total similarity: {total}")
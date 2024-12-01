left = []
right = []

with open("input.txt", "r") as file:
    for line in file:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

assert len(left) == len(right), "Length of left and right should be same"

left.sort()
right.sort()

total_diff = 0
for i in range(len(left)):
    total_diff += abs(left[i] - right[i])

print(f"Total difference: {total_diff}")

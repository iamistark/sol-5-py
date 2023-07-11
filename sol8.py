from collections import defaultdict

def find_original(changed):
    original = []
    counts = defaultdict(int)

    for num in changed:
        counts[num] += 1

    for num in changed:
        if counts[num] == 0:
            continue

        if counts[2 * num] == 0:
            return []

        original.append(num)
        counts[num] -= 1
        counts[2 * num] -= 1

    return original
#Driver code
changed = [1, 3, 4, 2, 6, 8]
result = find_original(changed)
print(result)

count = 0
therteen_count = 0

for i in range(int(1e6)):
    nums_l = [int((i // 1e3) % 10), int((i // 1e4) % 10), int((i // 1e5) % 10)]

    nums_r = [int(i % 10), int((i % 100) // 10), int((i % 1000) // 100)]

    if sum(nums_l) == sum(nums_r):
        count += 1
        if (sum(nums_l) + sum(nums_r)) == 13:
            therteen_count += 1
print(f"2.1: {count} \n2.2: {therteen_count}")
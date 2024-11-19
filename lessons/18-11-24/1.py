
with open("./files/numbers.txt", "r") as nums:
    nums = [int(n.strip()) for n in nums.readlines()]
    print(sum(nums))
    
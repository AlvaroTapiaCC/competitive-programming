
def modify_set(nums: set, n: int):
    nums.discard(n)


nums = set(range(1, 6))

modify_set(nums, 3)

print(nums)
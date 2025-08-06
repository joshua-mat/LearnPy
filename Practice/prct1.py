
def twoSum(nums: list[int], target: int) -> list[int]:
    i = 0
    ls = list()
    while i < len(nums):
        for n in range(len(nums)):
            if nums[i] + nums[n+1] == target:
                print(i, n)
                print(nums[i] + nums[n])
                ls = [i, n]
        i += 1
    return ls

ls = twoSum([3,2,3], 6)
print(ls)
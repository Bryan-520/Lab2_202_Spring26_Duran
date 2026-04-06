
def search(nums:list[int], target: int, idx:int = 0)->int:
    #idx isn't used in this implentation but you will need it for recursive
    #convert to recursive
    if idx >= len(nums):
        return -1
    if nums[idx] == target:
        return idx
    return search(nums, target, idx + 1)
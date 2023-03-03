def find_duplicate(nums):
    if not all(isinstance(num, int) and num >= 0 for num in nums):
        return False

    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return False

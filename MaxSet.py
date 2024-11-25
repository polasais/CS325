# Name: Isac Polasak
# OSU Email: Polasais@oregonstate.edu
# Course: CS325

def max_independent_set(nums):
    all_neg = 0            # We set that all vals are neg, then we check if it's true.
    for i in nums:
        if i > 0:
            all_neg = 1    # If not all vals are neg, then we make all_neg 1.
    if all_neg == 0:       # If all vals were neg, then we return an empty list.
        return []

    if len(nums) == 1:     # if just 1 num is listed, then just return that num.
        return [nums[0]]

    cache = [0]*len(nums)  # Cache will contain max at that index
    cache[0] = nums[0]                # if there's 2 nums, set the first cache to the first num.
    cache[1] = max(nums[0], nums[1])  # and the 2nd cache index to the max between the first two nums.

    for i in range(2, len(nums)):
        if nums[i] < 0:            # If the current num is neg, don't add it.
            cache[i] = cache[i-1]  # Instead, put the prev max in the current pos in the cache.
        else:                      # If it's pos then check if including the current is better than excluding it
            cache[i] = max((cache[i-2] + nums[i]), cache[i-1])

    nums_used = []
    index = len(nums) - 1   # Initialize index as last index in nums
    while index >= 0:       # While index ≥ 0, check if the current cache value is different to the prior cache value
        if index == 0 or cache[index] != cache[index-1]: # If there's a diff between current and prev val in cache
            if nums[index] > 0:     # Only include the positive numbers
                nums_used.append(nums[index])
            index = index-2         # Skip the previous index, as it's been used.
        else:
            index = index-1         # Otherwise, move back an index and check if the prev changed.
    nums_used.reverse()
    return nums_used

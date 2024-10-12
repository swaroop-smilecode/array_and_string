# Will solve the problem by 2 pointer approach.
# i = 0 , so that it points to first element 
# j = len(nums) - 1, so that it points to last element 

# Logic:
# keep incrementing i until you see 5 
# keep decrementing j until you see not 5
# swap i & j
# You should do this work until i < j. Whenever i value is 
# morethan j, then it means you have seen every element in 
# the input.
def five_sort(nums):
    i = 0
    j = len(nums) - 1
    while i<j:
        # keep incrementing i until you see 5
        if nums[i] != 5:
            i += 1
        # keep decrementing j until you see not 5
        if nums[j] == 5:
            j -= 1
        # swap i & j
        if nums[i] == 5 and nums[j] != 5:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    return nums

print(five_sort([12, 5, 1, 5, 12, 7])) # -> [12, 7, 1, 12, 5, 5]
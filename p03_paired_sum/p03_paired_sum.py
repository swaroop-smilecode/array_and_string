def pair_sum(numbers, target_sum):
    previous_numbers = {}
    for index, num in enumerate(numbers):
        complement_num = target_sum - num
        if complement_num in previous_numbers:
            return (index, previous_numbers[complement_num])
        previous_numbers[num] = index
    return False

pair_sum([3, 2, 5, 4, 1], 8) # -> (0, 2)

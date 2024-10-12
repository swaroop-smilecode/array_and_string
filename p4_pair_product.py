def pair_product(numbers, target_product):
    previous_numbers = {}
    for index, num in enumerate(numbers):
        complement_number = target_product / num
        if complement_number in previous_numbers:
            return (previous_numbers[complement_number], index)
        previous_numbers[num] = index
    return False

pair_product([3, 2, 5, 4, 1], 8) # -> (1, 3)
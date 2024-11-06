def most_frequent_char(s):
    count = {}

    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    early_appeared = None
    for char in count:
        if early_appeared is None or count[char] > count[early_appeared]:
            early_appeared = char
    
    return early_appeared

print(most_frequent_char('bookeeper')) # -> 'e'
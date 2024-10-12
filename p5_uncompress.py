def uncompress(s):
    numbers = {1,2,3,4,5,6,7,8,9}
    result = []
    i = 0
    j = 0

    while j < len(s):
        if s[j] in numbers:
            J += 1
        else:
            num = int(s[i:j])
            result.append(s[j]*num)
            j += 1
            i = j
    
    return "".join(result)

print(uncompress("2c3a1t")) # -> 'ccaaat'

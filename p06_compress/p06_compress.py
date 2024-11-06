def compress(s):
    # In a 2 pointer approach, there are 2 variations.
    # 1. Initialize i = 0 & j = len(n) --> Then keep coming towards middle of list
    # 2. Initialize both i = 0 & j = o --> First move j & then i --> But during this process, 
    # we need j to be at the index of len(s) + 1. But, if we do that, then will get index out of 
    # bound error. Hence, we are adding this !
    s += '!'

    # This is the second variation in 2 pointer approach. So, we are moving through the input 
    # using index j --> Then based on if & else conditions, performing the work that's needed.
    result = []
    i = 0
    j = 0
    while j < len(s):
        if s[i] == s[j]:
            j += 1
        else:
            num = j - i
            # When we compress the string, 1 should not be added if the number is getting repeated
            # only one time, That's why we have this num == 1 in place.
            if num == 1:
                result.append(s[i])
            else:
                result.append(str(num)+s[i])
            i = j
            num = 0
            print(result)
    
    return "".join(result)

print(compress('ccaaatsss')) # -> '2c3at3s'
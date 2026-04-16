def write_sequence(n: int):
    digits_added = 0
    for i in range(1, n+1):
        if len(str(i)) > 1:
            for j in str(i):
                digits_added += 1
             #   sequence.append(int(j))
        else:
            digits_added += 1
            #sequence.append(i)
    return digits_added

print(write_sequence(20))
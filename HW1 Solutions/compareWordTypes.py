def compare_Word_Types(str1, str2, norm):
    sameWordPOS = 0

    for i in str1:
        for j in str2:
            print(f'Comparing {i} and {j} \n')
            if i == j:
                sameWordPOS = sameWordPOS + 1
                print(f'Match found!\n \n')

    if norm == 'Y':
        return sameWordPOS / ((len(str1) + len(str2)) / 2)
    elif norm == 'N':
        return sameWordPOS
    else:
        return "Invalid parameter. should be Y or N for normalization (case sensitive)"

def value_count(data, value):
    # pocet vyskytu value v n*n poli
    radky = len(data)
    sloupce = len(data[0])
    counter =0
    for r in range(radky):
        for s in range(sloupce):
            if value == data[r][s]:
                counter +=1

    return counter

def value_positions(data, value):
    radky = len(data)
    sloupce = len(data[0])
    result = []
    for r in range(radky):
        for s in range(sloupce):
            if value == data[r][s]:
                result.append((r,s))

    return result

if __name__ == '__main__':
    value = -1
    data = [\
        [0,-1,1],
        [-1, 0, -1],
        [1,0,-1]]
    count = value_positions(data, value)
    print(count)
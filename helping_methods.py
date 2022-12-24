def find_sol1(x1, k):
    x = x1.upper()
    l1 = []
    l2 = []
    a = 65
    
    for i in range(26):
        l1.append(chr(i+65))
        
    for j in range(26):
        l2.insert(k, chr(a))
        k += 1
        a += 1
        if k > 25:
            k = 0
        if a > 91:
            break

    count = 0
    for i in l1:
        if i == x:
            return l2[count]
        else:
            count += 1


def find_sol2(x1, c):
    x = x1.upper()
    l1 = []
    
    for i in range(26):
        l1.append(chr(i+65))

    count = 1 + c
    for i in l1:
        if i == x:
            return count
        else:
            count += 1


def find_sol3(x1, k):
    x = x1.upper()
    l1 = []
    l2 = []
    a = 65

    for i in range(26):
        l1.append(chr(i + 65))

    for j in range(26):
        l2.insert(k, chr(a))
        k += 1
        a += 1
        if k > 25:
            k = 0
        if a > 91:
            break

    count = 0
    for i in l2:
        if i == x:
            return l1[count]
        else:
            count += 1

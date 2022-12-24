from helping_methods import *

ch = int(input("\n1. Encryption\n2. Decryption\nEnter your choice: "))
if ch == 1:
    a = input("\nEnter plain text: ")
    b = input("Enter keyword: ")
    c = int(input("Enter key value: "))
    l1 = []

    for i in b:
        l1.append(find_sol2(i, c))
    li = []

    t = 0
    for i in a:
        if t >= len(l1):
            t = 0
        if i == " ":
            li.append(" ")
        else:
            li.append(find_sol1(i, l1[t]-1))
            t += 1

    print("\nCipher text: ", end="")
    for i in li:
        print(i, end="")
    print()

elif ch == 2:
    a = input("\nEnter cipher text: ")
    b = input("Enter keyword: ")
    c = int(input("Enter key value: "))
    l1 = []

    for i in b:
        l1.append(find_sol2(i, c))
    li = []

    t = 0
    for i in a:
        if t >= len(l1):
            t = 0
        if i == " ":
            li.append(" ")
        else:
            li.append(find_sol3(i, l1[t] - 1))
            t += 1

    print("\nPlain text: ", end="")
    for i in li:
        print(i, end="")
    print()

else:
    print("\nWrong choice!")

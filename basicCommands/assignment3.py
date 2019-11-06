s = "aaaaaabbbbbbbbccccccccccdddddddddeeeeffffffffxyzz"

# for i in s:
#     print(i)

def countChar(stringToCount):
    old = s[0]
    dict = {}
    counter = 1
    for i in s:
        while(i is not old):
            # dict[old]=counter
            old = i
            counter=1
        else:
            dict[old] = counter
            counter += 1
    return dict

print(countChar(s))




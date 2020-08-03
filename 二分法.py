def binary_research(find_num,l):
    print(l)
    len1 = len(l)
    if find_num>l[len1//2]:
        l=l[len1//2:len1:1]
        binary_research(find_num,l)
    elif find_num<l[len1//2]:
        l=l[0:len1//2:1]
        binary_research(find_num,l)
    else:
        print(l[len1//2])

l=[1,2,4,5,7,8,9,14,25,64,78]
binary_research(5,l)
binary_research(64,l)
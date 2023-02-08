def unique(lst):
    
    ulst = []
    for i in lst:
        if i not in ulst:
            ulst.append(i)
    
    return ulst

lst = list(map(int,input().split()))

print(unique(lst))

def cd(n):
    
    for i in range(n, -1, -1):
        if (i==0):
            break
        yield i

n = int(input())
for num in cd(n):
    print(num)

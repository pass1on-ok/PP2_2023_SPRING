def even_numbers(n):
   
    i = 0
    while i <= n:
        if i % 2 == 0:
            yield i
        i += 1

n = int(input("Enter the value of n: "))

even_nums = even_numbers(n)
print("Even numbers between 0 and", n, "are:", end=" ")

for num in even_nums:
    print(num, end="")
    if num != n and (num != n-1 and num != n-2):
        print(",", end=" ")

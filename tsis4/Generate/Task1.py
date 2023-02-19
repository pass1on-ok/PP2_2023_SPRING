def square_generator(N):
   
    i = 1
    while i <= N:
        yield i*i
        i += 1

N = int(input())
for square in square_generator(N):
    print(square)

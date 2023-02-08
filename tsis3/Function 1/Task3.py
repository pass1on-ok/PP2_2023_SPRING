def solve(numheads, numlegs):
  numchickens = (2 * numheads) - numlegs // 2
  numrabbits = numheads - numchickens
  print(numchickens, numrabbits)

nh, nl = map(int,input().split())
solve(nh,nl)

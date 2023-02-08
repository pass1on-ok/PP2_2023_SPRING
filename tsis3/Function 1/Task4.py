def filter_prime(nums): 
  result = []
  
  for num in nums: 
    is_prime = True
    if num > 1: 
      for i in range(2, num): 
        if (num % i) == 0: 
          is_prime = False
          break
      if is_prime: 
        result.append(num)
  return result

num = list(map(int,input().split()))

print(filter_prime(num))

import itertools 
  

def permutation(string): 
    
    permList = list(itertools.permutations(string)) 
  
    count = 0
    for perm in permList: 
        print(''.join(perm))
        
  

if __name__ == "__main__": 
    string = input() 
    permutation(string)

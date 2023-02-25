
import re


pattern = r'a(b)'


test_strings = ['ab', 'abb', 'abbb', 'ac', 'abc']


for test_string in test_strings:
   
    match = re.match(pattern, test_string)
    
    
    if match:
        print('{test_string} matches'.format(test_string=test_string))
    
    else:
        print('{test_string} does not match'.format(test_string=test_string))

import re


pattern = r'a(bb|bbb)'


test_strings = ['ab', 'abb', 'abbb', 'abbbb', 'ac', 'abc']


for test_string in test_strings:
    
    match = re.match(pattern, test_string)
    
   
    if match:
        print('{test_string} match'.format(test_string=test_string))
    
    else:
        print('{test_string} does not match'.format(test_string=test_string))

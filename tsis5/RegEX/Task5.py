import re


pattern = r'a.*b$'


test_strings = ['acb', 'aab', 'aBc', 'abc', 'abcde', 'ab']


for test_string in test_strings:
    
    match = re.match(pattern, test_string)
    
    
    if match:
        print('{test_string} match'.format(test_string=test_string))
    else:
        print('{test_string} does not match'.format(test_string=test_string))

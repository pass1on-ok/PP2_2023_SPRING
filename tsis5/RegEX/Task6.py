import re


pattern = r'[ ,.]'


test_string = 'This is a test, string. With some spaces and commas.'


new_string = re.sub(pattern, ':', test_string)


print('Original string:', test_string)
print('New string:', new_string)

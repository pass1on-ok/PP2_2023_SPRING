import re


pattern = r'[A-Z][a-z]+'


test_string = 'This is a Test String with Some Matching Patterns'


matches = re.findall(pattern, test_string)


print(matches)

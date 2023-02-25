import re


pattern = r'([a-z])([A-Z])'


test_string = 'HelloWorldHowAreYou'


new_string = re.sub(pattern, r'\1 \2', test_string)


print('Original string:', test_string)
print('New string:', new_string)

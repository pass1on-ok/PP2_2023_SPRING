
import re


test_string = 'HelloWorldHowAreYou'

split_string = re.findall('[A-Z][^A-Z]*', test_string)

print('Original string:', test_string)
print('Split string:', split_string)

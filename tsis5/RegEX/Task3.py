import re

pattern = r'[a-z]+_[a-z]+'


test_string = 'this_is_a_test_string_with_some_matching_patterns'


matches = re.findall(pattern, test_string)


print(matches)

import re

pattern = r'_([a-z])'


snake_string = 'hello_world_how_are_you'

camel_string = re.sub(pattern, lambda match: match.group(1).upper(), snake_string)


camel_string = camel_string[0].upper() + camel_string[1:]


print('Original string:', snake_string)
print('Camel case string:', camel_string)

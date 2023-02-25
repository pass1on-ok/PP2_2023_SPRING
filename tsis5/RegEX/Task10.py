import re

camel_string = 'HelloWorldHowAreYou'


snake_string = re.sub(r'(?<!^)(?=[A-Z])', '_',camel_string).lower()

print('Original string:', camel_string)
print('Snake case string:', snake_string)

import re
pattern = re.compile('test')
r = re.findall(pattern, 'test testmore test')
print('match: ')
print(r)

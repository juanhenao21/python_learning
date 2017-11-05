lookup = {}
lookup = dict()
lookup = {'age': 42, 'loc': 'Italy'}
lookup = dict(age=42, loc='Italy')

print(lookup)
print(lookup['loc'])


lookup['cat'] = 'Fun code demos'

if ('cat' in lookup):
    print(lookup['cat'])
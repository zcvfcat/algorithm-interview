
import collections


a = dict()
a = {}

a = {
    'key1': 'value1',
    'key2': 'value2'
}

a['key3'] = 'value3'

print(a)

try:
    print(a['key4'])
except KeyError:
    print('존재하지 않는 키')

# 딕셔너리 모듈

a = collections.defaultdict(int)

a['A'] = 5
a['B'] = 4
a['C'] += 1
print(a)

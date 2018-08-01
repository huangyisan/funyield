import json

a = {'a': 1, 'b': 0, 'd': 'd', 'f': '1.1'}
b = '{"a": 1, "b": 0, "d": "d", "f": "1.1"}'

# with open('test.list', 'w') as f:
#     json.dump(a, f)


print(json.dumps(a))

# with open('test.list', 'r') as f:
#     result = json.load(f)

print(json.loads(b))

# print(result)
import json
str_a = '{"a": 1,"b": 0,"d": "d","f": "1.1"}'
dict_a = {'a': 1, 'b': 0, 'd': 'd', 'f': '1.1'}
print(json.dumps(str_a), ' '*5, type(json.dumps(str_a)))
print(json.dumps(dict_a), ' '*5, type(json.dumps(dict_a)))

print(json.loads(str_a), ' '*5, type(json.loads(str_a)))
# print(json.loads(dict_a), ' '*5, type(json.loads(dict_a)))

# dumps(字典，类json字符串) --> 产出为类json字符串
# loads(类json字符串) --> 产出为字典

with open('test.list','w') as f:
    json.dump(str_a, f)

with open('test.list','r') as f:
    data = json.load(f)
print('*'*5)
print(data, ' '*5, type(data))

# dump(类json字符串 或者 字典) ———— 将dumps的内容写入文本
# load(类json字符串 或者 字典)从文本读出 ———— 文本内容样式为str则产出是str，文本内容样式是字典则产出是字典
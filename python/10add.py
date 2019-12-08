num = 4
count = 3
res = sum(map(lambda x:x* 10 ** (count-x) *num, range(0,count+1)))
print(res)
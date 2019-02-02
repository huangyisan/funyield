from functools import partial
# range(m,n) 为原函数
print(list(range(2,11)))

# 将range函数中的第一个数字2冻结
par = partial(range, 2)

# 至此par通过range和给定的参数2构建了一个新的函数，功能为range(2,x)
# 进行内容输出
print(par(11))
print(list(par(11)))
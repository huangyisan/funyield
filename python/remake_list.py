lst = [1,2,3,4,5]
new_lst =list(map(lambda x:x[0]-x[1], [(x,lst[0]) for x in lst]))
print(new_lst)

def max_index(a_list):
    old_list = a_list[:]
    a_list.sort(reverse=True)
    if a_list[0] >= 2 * a_list[1]:
       return old_list.index(a_list[0])
    return -1

a_list = [3,6,2,1]
b_list = [4,6,2,1]
c_list = [3,4,10,2,5]

print(max_index(a_list))
print(max_index(b_list))
print(max_index(c_list))



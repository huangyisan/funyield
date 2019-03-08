import copy

w = [1,2,3,4,4,5,6]

for i in copy.deepcopy(w):
    if i == 4:
        w.remove(i)
print(w)

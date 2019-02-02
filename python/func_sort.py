a = "hUangYisan6749"
def custom_order(x):
    if x.islower():
        return 1,0,0,0,x
    if x.isupper():
        return 0,1,0,0,x
    if x.isdigit() and int(x) % 2 == 0:
        return 0,0,1,0,x
    else:
        return 0,0,0,1,x

print("".join(sorted(a,key=custom_order)))
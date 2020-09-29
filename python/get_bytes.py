Bytes = ''
for bit in range(1,5):
    # print(1<<bit)
    # print(str(bin(5&(1<<bit))))
    # print(str(bin(5&(1<<bit))).split('0b')[1])
    # Bytes += str(ord(5&(1<<bit))).split('0b')[1]
    Bytes += str(5&(1<<bit))

print(Bytes)
import hashlib

class BloomFilter(object):
    def __init__(self,size):
        self.size = size
        self.arrarylist = [0]*size
        self.hash_func = [hashlib.md5, hashlib.sha1, hashlib.sha224]

    def add_data(self,data):
        for func in self.hash_func:
            index = int(func(data.encode()).hexdigest(),16) % self.size
            self.arrarylist[index] = 1



    def is_data_exist(self,data):
        result = 1 #起始位为1，如果为0，则肯定最终结果为0了。
        for func in self.hash_func:
            index = int(func(data.encode()).hexdigest(),16) % self.size
            result &= self.arrarylist[index]

        return True if result == 1 else False

if __name__ == '__main__':
    bf_size = 100

    bloom_filter = BloomFilter(bf_size)

    arrarylist = []

    for i in range(100):
        bloom_filter.add_data(str(i))
    print(bloom_filter.arrarylist)

    # print(bloom_filter.is_data_exist(str(1)))

    for i in range(1000):
        print(bloom_filter.is_data_exist(str(i)))
    

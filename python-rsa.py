#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Create Time: 2016/11/27 13:03:06
# Create author: XiaoFengfeng


class pyrsa(object):
    def __init__(self, p, q):
        """
            只是实现一个rsa计算过称
        """
        self.q = q
        self.p = p

        self.decrypt = self.encrypt
        self.bits = self.get_bits()

    def range_prime(self, start, end):
        """
            获得一个数值范围内的所有质数
        """
        prime_list = list()
        for num in range(start, end + 1):
            for e in range(2, num):
                if num % e == 0:
                    break
            else:
                prime_list.append(num)

        return prime_list

    def generate_keys(self):
        """
            获得公钥和私钥
        """
        q = self.q
        p = self.p

        prime_list = self.range_prime(11, 1000)
        N = p * q
        T = (p - 1) * (q - 1)

        e1 = 0
        for pri in prime_list:
            if pri < T and T % pri != 0:
                e1 = pri
                break
        else:
            raise Exception("e1 not found.")

        x = 0
        e2 = 0
        while x < T // e1:
            if (T * x + 1) % e1 == 0:
                e2 = (T * x + 1) // e1
                break
            x += 1
        else:
            raise Exception("e2 not found")

        print("e2:", e2)

        return (N, e1), (N, e2)

    def encrypt(self, m, key):
        """
            加解密m（解密时只是m换成了密文）
        """
        N, e = key
        return (m ** e) % N

    def get_bits(self):
        bit = len(bin(self.q * self.p)) - 2
        return bit


if __name__ == '__main__':
    import time
    start = time.clock()

    pr = pyrsa(991, 997)
    public, private = pr.generate_keys()
    print("public:", public, "private:", private)

    C = range(20, 30)
    C = [key for key in C]

    E = map(lambda x: pr.encrypt(x, public), C)
    E = [key for key in E]

    D = map(lambda x: pr.decrypt(x, private), E)
    D = [key for key in D]

    print("Message:", C)
    print("Encrypt:", E)
    print("Decrpyt:", D)

    print("Bits:", pr.bits)

    end = time.clock()
    runtime = end - start
    print("Python Finished in {0:.4}s".format(runtime))

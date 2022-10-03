import random, os, sys

class methallylxetamin():

    # 512 bit key seed, 64 bytes, in theory

    key = [
        0x43111198, 0x71994491, 0xc9c0fbcf, 0xdeb5dba5, 0xbb56c25b, 0xaaf111f1,
        0x9f3f82a4, 0xbb1c5ed5, 0x4f07aa98, 0x22235b01, 0xfc3185be, 0xde0c7dc3,
        0xbbbe5d74, 0xaadeb1fe, 0x9fbda6a7, 0xaa9bf174, 0xe56b69c1, 0xef334786,
        0xeac19dc6, 0xde0ca1cc, 0xbbe92c6f, 0xaa7484aa, 0xfcb0a9dc, 0xccf988da,
        0x182e5152, 0xa844c66d, 0xee0327c8, 0xde597fc7, 0xcbe00bf3, 0xaaa79147,
        0xf6ca6351, 0xdd292967, 0x27333a85, 0x11ff2138, 0xee2c6dfc, 0xde380d13,
        0xcb0a7354, 0xaa6a0abb, 0xf1c2c92e, 0xee722c85, 0xa2bfe8a1, 0xa22a664b,
        0xee4b8b70, 0xde6c51a3, 0xaa92e819, 0xaa990624, 0xf40e3585, 0xff6aa070,
        0x11c44146, 0x11376ff8, 0xee48774c, 0xdeb0bcb5, 0x1a1c0cb3, 0xaad8aa4a,
        0xfb9cca4f, 0xff2e6ff3, 0x949f82ee, 0x652263ff, 0xedc87814,
        0xfabefffa, 0xa650aceb, 0xfef9a3f7, 0xff7178f2, 0xff12344f
    ]

    def __init__(self, key=[]):
        if len(key) != 0:
            self.key = key

        print("Key seed size is %d" %sys.getsizeof(self.key))

        ri = random.randint(0,63)
        print("Random byte from key of index %d: %d" %(ri, self.key[ri]))

        print("Reading 64 bytes of real entropy")
        rd = open("/dev/random", 'rb')
        entropy = rd.read(64)
        print("Done.")
    
        print("Randomizing key with XOR")
        for i in range(64):
            self.key[i]  ^= (entropy[i] ** rd.read(1)[0])
        rd.close()
        print("Done.")
        
        print("New key size is %d" %sys.getsizeof(self.key))

    print("Key generated.")


import random

length = 200

def rand_string():
    ret = ''
    t = 20

    for _ in range(length // t):
        cur = bin(random.randint(0, (1 << t) - 1))[2:]
        cur = cur.zfill(t)
        ret += cur

    if len(ret) != length:
        raise Exception('wrong string length of %d, 200 expected' % len(ret))

    return ret

    # return ''.join([str(random.randint(0, 1)) for _ in range(length)])

if __name__ == "__main__":
    pass

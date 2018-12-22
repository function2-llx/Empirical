import random

length = 200

def rand_string():
    ret = ''
    t = 20

    for _ in range(length // t):
        ret += bin(random.randint(0, (1 << t) - 1))[2:].zfill(t)

    if len(ret) != length:
        raise Exception('wrong string length of %d, 200 expected' % len(ret))

    return ret
    
if __name__ == "__main__":
    pass

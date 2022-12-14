import random
from typing import Tuple, List, AnyStr


def write(filename: str, string: AnyStr) -> None:
    with open(f'{filename}', 'w') as file:
        file.write(string)


def split_seq(seq, l: int) -> List:
    res = []
    for i in range(0, len(seq), l):
        res.append(seq[i: i + l])
    return res


def to_bin(n: int) -> str:
    s = bin(n)[2:]
    s = '0' * ((8 - (len(s) % 8)) % 8) + s
    return s


def generate_big_prime(size: int) -> int:
    print('[+] Generating prime number...')
    n = 4
    left, right = int(1.5 * (1 << (size - 1))), (1 << size) - 1
    while not is_prime(n):
        n = random.randint(left, right)
    return n


def phi(p: int, q: int) -> int:
    return (p - 1) * (q - 1)


def is_prime(n: int) -> bool:
    if not n & 1:
        return False
    t = 20
    for i in range(t):
        a = random.randint(2, n - 1)
        r = fast_pow(a, n - 1, n)
        if r != 1:
            return False
    return True


def euclede_ext(a: int, b: int) -> Tuple[int, int, int]:
    if a < b:
        a, b = b, a
    x2, x1, y2, y1 = 1, 0, 0, 1
    while b > 0:
        q = a // b
        r = a - q * b
        x = x2 - q * x1
        y = y2 - q * y1
        a, b = b, r
        x2, x1, y2, y1 = x1, x, y1, y
    return a, x2, y2


def fast_pow(a: int, k: int, n: int) -> int:
    if k == 0:
        return 1
    b = a if k & 1 else 1
    A = a
    k >>= 1
    while k:
        A = (A * A) % n
        if k & 1:
            b = (A * b) % n
        k >>= 1
    return b

from src.functions import *
from src.encrypt import encrypt
from src.decrypt import decrypt
from src.keys_funcs import generate_keys


def attack1():
    SIZE = 256
    e, n, d = generate_keys(SIZE, private=True)
    # Перехватываем шифрованное сообщение
    write('input.txt', 'Hello, World!')
    intercepted_msg = int(encrypt((e, n), SIZE), 16)

    x = random.randint(1, n - 1)
    while euclede_ext(x, n)[0] != 1:
        x = random.randint(1, n - 1)

    y = (intercepted_msg * fast_pow(x, e, n)) % n
    # Получаем дешифровку кастомного сообщения
    write('input.txt', hex(y)[2:])
    decrypted = decrypt((e, n, d), decode=False)[0]

    p = (decrypted * euclede_ext(x, n)[2]) % n
    p_text = bytearray(map(lambda i: int(i, 2), split_seq(to_bin(p), 8)))
    print('Source message:', p_text.decode('utf-8'))


def attack2():
    SIZE = 32
    n1, n2, n3 = generate_keys(SIZE)[1], generate_keys(SIZE)[1], generate_keys(SIZE)[1]
    with open('input.txt', 'w') as f:
        f.write('Privet')
    c1, c2, c3 = encrypt((3, n1), SIZE), encrypt((3, n2), SIZE), encrypt((3, n3), SIZE)
    c_list, n_list = [int(c1, 16), int(c2, 16), int(c3, 16)], [n1, n2, n3]
    N = n1 * n2 * n3
    x = 0
    for i in range(3):
        Ni = N // n_list[i]
        _, _, inv = euclede_ext(Ni, n_list[i])
        x += c_list[i] * Ni * inv
    x %= N

    def find_invpow(x, n):
        high, mid = 1, 0
        while high ** n < x:
            high *= 2
        low = high // 2
        while low < high:
            mid = (low + high) // 2
            if low < mid and mid ** n < x:
                low = mid
            elif high > mid and mid ** n > x:
                high = mid
            else:
                return mid
        return mid + 1

    x = find_invpow(x, 3)
    p_text = bytearray(map(lambda j: int(j, 2), split_seq(to_bin(x), 8)))

    print('Source message:', p_text.decode('utf-8'))


def attack3():
    SIZE = 512
    mod = 2 * SIZE
    p, q = generate_big_prime(SIZE), generate_big_prime(SIZE)
    phi_n = (p - 1) * (q - 1)
    n = p * q
    e = 3
    d = euclede_ext(phi_n, e)[2] % phi_n
    d0 = d % (2 ** (mod // 4))

    for k in range(0, e + 1):
        a = k
        b = k * n + k + 1 - e * d0
        p = mod
        gcd = euclede_ext(a, p)[0]
        if gcd > 1 and b % gcd:
            continue
        a //= gcd
        b //= gcd
        p //= gcd
        inverse_a = euclede_ext(a, p)[2]
        x0 = (inverse_a * b) % p
        x_list = []
        for i in range(1, gcd + 1):
            x_list.append((x0 + (i - 1) * p) % (p * gcd))
        print('Решения: s =', x_list)

        # s = n + 1 - (e * d0 - 1) // k % (2 ** (mod // 4))
        # D = s * s - 4 * n
        # p1 = (s + int(math.pow(D, 1/2))) // 2
        # p2 = (s - int(math.pow(D, 1/2))) // 2
        # pk = min(p1, p2, key=lambda x: abs(x - p))
        # if minimum[0] > abs(pk - p):
        #     minimum = (abs(pk - p), pk)

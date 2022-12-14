from src.functions import *


def generate_keys(SIZE: int, private=False) -> Tuple[int, int] | Tuple[int, int, int]:
    p, q = generate_big_prime(SIZE), generate_big_prime(SIZE)
    phi_n = (p - 1) * (q - 1)
    n = p * q
    e = 65537
    d = euclede_ext(phi_n, e)[2] % phi_n

    with open('keys/public_key.txt', 'w') as public:
        public.writelines([hex(e)[2:] + '\n', hex(n)[2:] + '\n'])
    print('[+] Public key generated in file: public_key.txt')

    if private:
        with open('keys/private_key.txt', 'w') as private:
            private.write(hex(d)[2:])
        print('[+] Private key generated in file: private_key.txt')
        return e, n, d

    return e, n


def read_keys(private=False) -> Tuple[int, int] | Tuple[int, int, int]:
    with open('keys/public_key.txt', 'r') as pub:
        e, n = pub.readlines()
        e, n = int(e.strip(), 16), int(n.strip(), 16)
    if private:
        with open('keys/private_key.txt', 'r') as private:
            d = int(private.read().strip(), 16)
        return e, n, d

    return e, n

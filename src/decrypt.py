from src.functions import *


def decrypt(private_key: Tuple[int, int, int], decode=True):
    e, n, d = private_key
    with open('input.txt', 'r', encoding='utf-8') as file:
        text = file.readlines()

    new_text_blocks = []
    block_ints = []
    for block in text:
        block_n = fast_pow(int(block.strip(), 16), d, n)
        num = to_bin(block_n)
        bts = bytearray(map(lambda x: int(x, 2), split_seq(num, 8)))
        block_ints.append(block_n)
        if decode:
            new_text_blocks.append(bts.decode('utf-8'))
    if decode:
        write('output.txt', ''.join(new_text_blocks))

    print('Text successfully decrypted!')
    return block_ints

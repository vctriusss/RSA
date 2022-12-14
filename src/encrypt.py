from src.functions import *


def encrypt(public_key: Tuple[int, int], SIZE: int):
    e, n = public_key
    with open('input.txt', 'r', encoding='utf-8') as inp:
        text = bytearray(inp.read(), 'utf-8')

    text_blocks = split_seq(list(text), 2 * SIZE // 8)
    new_blocks = []

    for block in text_blocks:
        block_n = ''.join(to_bin(b) for b in block)
        block_n = int(block_n, 2)
        block_n = fast_pow(block_n, e, n)
        new_blocks.append(hex(block_n)[2:])

    write('output.txt', '\n'.join(new_blocks))
    print('Text successfully encrypted!')
    return '\n'.join(new_blocks)

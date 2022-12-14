from src.functions import *
from src.attacks import attack1, attack2, attack3
from src.encrypt import encrypt
from src.decrypt import decrypt
from src.keys_funcs import generate_keys, read_keys


def main():
    SIZE = 512
    mode = 3
    while mode == 3:
        mode = int(input('Выберите режим работы:\n'
                         '1) Зашифровать текст\n'
                         '2) Расшифровать текст\n'
                         '3) Сгенерировать ключи\n'
                         '4) Криптоатаки\n'))
        if mode == 1:
            encrypt(read_keys(), SIZE)
        elif mode == 2:
            decrypt(read_keys(private=True))
        elif mode == 3:
            generate_keys(SIZE, private=True)
        elif mode == 4:
            option = int(input('Выберите тип атаки:\n'
                               '1) Аттака с выборкой зашифрованного текста\n'
                               '2) Аттака 2\n'
                               '3) Аттака 3\n'))
            exec(f'attack{option}()')


if __name__ == '__main__':
    main()

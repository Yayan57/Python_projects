def main():
    equals_debugging()


def equals_debugging():
    str_value = 'other'
    num_value = 123
    print(f'the value is {str_value}')
    print(f'{str_value=}')
    print(f'{num_value % 2 =}')


if __name__ == '__main__':
    main()

def main(a, b):
    return a + b


assert main(123456789, 673243342) == 796700131

if __name__ == '__main__':
    with open('input.txt') as input_:
        input_str = input_.read()

    a, b = map(int, input_str.split())
    result = main(a, b)
    print(result)

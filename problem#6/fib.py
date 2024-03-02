def fibonacci(n):
    a = 0
    b = 1
    c = 1

    if(n < 0):
        return -1
    print()


if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')
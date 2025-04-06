def fibonachi_version(number_version):
    number_version = int(number_version)  # ← Преобразуем строку в число
    ver_fib = [0, 1]

    for a in range(len(ver_fib), number_version + 1):
        ver_fib.append(ver_fib[a-2] + ver_fib[a-1])
    return ver_fib[number_version] + ver_fib[number_version - 1]


if __name__ == '__main__':
    version = input()
    print(fibonachi_version(version))

def binAddCarry(a, b):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    result = ''
    carry = 0
    flag = False

    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result

        carry = 0 if r < 2 else 1
    if carry != 0:
        flag = True
        return [result.zfill(max_len), flag]
    else:
        return [result.zfill(max_len), flag]


def fracToBin(n):
    binary = str()

    while (n):
        n *= 2

        if (n >= 1):
            int_part = 1
            n -= 1
        else:
            int_part = 0

        binary += str(int_part)
    return binary


def intTo32bin(n):
    sign_bit = 0

    if (n < 0):
        sign_bit = 1

    n = abs(n)

    int_str = bin(int(n))[2:32]

    fraction_str = fracToBin(n - int(n))

    if (n == 0):
        return ['0', '00000000', '00000000000000000000000']
    else:
        index = int_str.index('1')
        exponent = bin((len(int_str) - index - 1) + 127)[2:]
        exponent = '0' * (8 - len(exponent)) + exponent
        mantissa = int_str[index + 1:23] + fraction_str
        mantissa = mantissa + ('0' * (23 - len(mantissa)))
        if (len(mantissa) > 23):
            mantissa = bin(int(mantissa[0:23], 2) + 1)[2:]
            mantissa = '0' * (23 - len(mantissa)) + mantissa
        return [sign_bit, exponent, mantissa]


def binDiv(num1, num2):
    if (num2 == 0):
        print("Деление на 0 запрещено!")
    elif (num1 == 0):
        return intTo32bin(0.0)
    else:
        num1, num2 = intTo32bin(num1), intTo32bin(num2)
        print("\t" + str(num1[0]) + " | " + num1[1] + " | " + num1[2] + "\n/\t" +
              str(num2[0]) + " | " + num2[1] + " | " + num2[2])
        print("-" * 42)
        temp1 = '1' + num1[2]
        temp2 = '1' + num2[2]
        mantissa = int(temp1, 2) / int(temp2, 2)

        tmp = 0
        if mantissa < 1:
            mantissa += 1
            tmp = 1

        mantissa = intTo32bin(mantissa)
        mantissa = mantissa[2]
        exponent = bin(int(num1[1], 2) - int(num2[1], 2) + 127 - tmp)[2:]
        exponent = '0' * (8 - len(exponent)) + exponent
        signbit = num1[0] ^ num2[0]
        return [signbit, exponent, mantissa]


def bin32toInt(bin):
    signbit = bin[0]
    exponent = int(bin[1], 2) - 127
    mantissa = bin[2]
    mantissa_int = 0
    power_count = -1

    for i in mantissa:
        mantissa_int += (int(i) * pow(2, power_count))
        power_count -= 1
    mantissa_int += 1
    number = pow(-1, signbit) * mantissa_int * pow(2, exponent)
    return number


if __name__ == "__main__":
    while (True):
        print("Введите 2 числа в 10 СС:")
        a = float(input("Делимое = "))
        b = float(input("Делитель = "))
        print(
            "Выберите действие:\n1: Деление\n2: Смена чисел"
        )
        inp = int(input("Сделайте выбор: "))

        while (inp != 2):
            if (inp == 1):
                quotient = binDiv(a, b)
                if (b == 0):
                    pass
                else:
                    print("\t" + str(quotient[0]) + " " + quotient[1] + " " +
                          quotient[2])
                    print("В десятичной СС: ", bin32toInt(quotient))
            print(
                "Выберите действие:\n1: Деление\n2: Смена чисел"
            )
            inp = int(input("Сделайте выбор: "))

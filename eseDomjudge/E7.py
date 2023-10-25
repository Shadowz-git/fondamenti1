def main() -> None:
    n = int(input())
    print(numberToRoman(n), end='')


def numberToRoman(number: int):
    migliaia = ["", "M"]
    centinaia = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    decine = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    unita = ["", 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

    m = number//1000
    if m != 0:
        m = migliaia[1]*m
    else:
        m = migliaia[0]
    c = centinaia[(number % 1000)//100]
    d = decine[(number % 100) // 10]
    u = unita[number % 10]

    return m + c + d + u


main()

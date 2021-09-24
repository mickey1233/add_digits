def adddigits(num):
    # 解一(自己)
    while num >= 0:
        num = str(num)
        sum = 0
        if len(num) == 1:
            return int(num)
        for i in num:
            sum += int(i)
        num = sum
    # 解二(別人leetcode)
    # if num == 0:
    #    return 0

    # if num%9 == 0:
    #    return 9
    # return num%9


def main():
    print(adddigits(38))
    print(adddigits(0))
    print(adddigits(5))
    print(adddigits(15985))


if __name__ == "__main__":
    main()

def ktraSn(n):
    if n < 0:
        return False
    else:
        s = []
        for i in range(1, n+1):
            if n % i == 0:
                s.append(i)
        return s


def main():
    a = int(input())
    if a > 0 and a <= 100:
        for i in range(1, a + 1):
            n = int(input())
            if n > 0:
                result = str(ktraSn(n))[1:-1]
                print(f"Test {i}: {result}")
            else:
                print("INVALID")
    else:
        print("Không hợp lệ !!")


if __name__ == '__main__':
    main()

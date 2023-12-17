# a,b = input().split()
## Bai1:
# print("Nhập 2 ố a và b: ")
# a, b = map(int, input().split())
# if a == b:
#     print("EQUAL")
# else:
#     print(f"DIFFIRENT {abs(a - b)}")

##Bai2:
# print("Nhập 3 số a,b,c : ")
# a, b, c = map(int, input().split())
# if (a + b > c) and (a + c > b) and (b + c > a):
#     print("YES")
# else:
#     print(f"NO")

##Bai3:
# def ktraSnt(n):
#     if n < 2:
#         return False
#     else:
#         for i in range(2, n):
#             if n % 1 == 0 and n % i == 0:
#                 return False
#         else:
#             return True
#
#
# def main():
#     a = int(input("Nhập số bộ test: "))
#     for i in range(1, a + 1):
#         n = int(input())
#         result = "YES" if ktraSnt(n) else "NO"
#         print(f"Test {i}: {result}")
#
#
# if __name__ == '__main__':
#     main()


##Bai4:
# def tinh(n):
#     if n < 0:
#         return False
#     else:
#         s = 0
#         for i in range(1, n):
#             s += n % 10
#             n //= 10
#     return s
#
#
# def main():
#     a = int(input("Nhập số bộ test: "))
#     for i in range(1, a + 1):
#         n = int(input())
#         result = f"{tinh(n)}" if tinh(n) else "IVAILID"
#         print(f"Test {i}: {result}")
#
#
# if __name__ == '__main__':
#     main()

##Bai5:

# def tinh(a, b, choose):
#     result = 0
#     loi = "ERROR"
#     if choose == '+':
#         result = a + b
#     elif choose == '-':
#         result = a - b
#     elif choose == '*':
#         result = a * b
#     elif choose == '/':
#         if b != 0:
#             result = a / b
#         else:
#             return loi
#     return result
#
#
# def main():
#     bt = input("Nhập biểu thức cần tính: ")
#     try:
#         a, choose, b = bt.split()
#         a, b = float(a), float(b)
#         result = tinh(a, b, choose)
#         print(f"{a} {choose} {b} = {result}")
#     except ValueError:
#         print("Định dạng đầu vào không hợp lệ.")
#
#
# if __name__ == "__main__":
#     main()
##Bai6:

# def tinh(choose):
#     result = 0
#     loi = "IVALID"
#     if choose == 1:
#         result = "Monday"
#     elif choose == 2:
#         result = "Tuesday"
#     elif choose == 3:
#         result = "Wendnesday"
#     elif choose == 4:
#         result = "Thurday"
#     elif choose == 5:
#         result = "Friday"
#     elif choose == 6:
#         result = "Saturday"
#     elif choose == 7:
#         result = "Sunday"
#     else:
#         return loi
#     return result
#
#
# def main():
#     n = int(input("Nhập số nguyên n: "))
#     print(tinh(n))
#
#
# if __name__ == '__main__':
#     main()


##Bai7:

# def gcd(a, b):
#     if a and b >0:
#         while b != 0:
#             a, b = b, a % b
#         return a
#
#
# def lcm(a, b):
#     return (a * b) // gcd(a, b)
#
# def main():
#     print("Nhập 2 số a và b: ")
#     a, b = map(int, input().split())
#     if a > 0 and b > 0:
#         print(f"{gcd(a,b)} {lcm(a,b)}")
#     else:
#         print("IVALID")
#
#
# if __name__ == '__main__':
#     main()
 ##Bai8:

def tongBinhPhuong(n):
    if n < 0:
        return False
    else:
        s = 0
        for i in range(1, n):
            s += (n % 10)**2
            n //= 10
    return s

def main():
    try:
        n = int(input("Nhập số nguyên dương n: "))

        if n <= 0:
            print("INVALID")
        else:
            result = tongBinhPhuong(n)
            print(result)

    except ValueError:
        print("INVALID")

if __name__ == "__main__":
    main()



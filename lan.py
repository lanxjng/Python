# a,b = input("Nhap a,b: ").split(",")
# print(f"{a}")
# print(f"{b}")
# print("Tong la: ",int(a) + int(b))
# print(f"Kieu dl la: {type(a)}")
# print(f"Kieu dl la: {type(b)}")
# Ctl + Alt + L : sua loi
# Ctrl + . : an code
# n = float(input(" Nhap n:"))
# if n > 0:
#     print("n > 0")
# elif n < 0:
#     print("n<0")
# else:
#     print("n=0")
# n = int(input("Nhap so n:"))
# for i in range(1,n+1,1):
#     print(i,end=", ")
# else:
#     print("Done")

# Cau truc Ham - "def ten_ham(thamso):"
# in ra cac so tu 1 den n chia het cho k
# n = int(input("NHap n:"))
# k = int(input("Nhap k :"))
# if k==0 or k>n:
#     print(f"Nhap lai k khac 0 va nho hon {n} !!!!")
# else:
#     for i in range(1,n+1,1):
#         if i % k ==0:
#             print(f"{i}", end=(","))
#     else:
#         print("Done!")

# def List_div_k(n, k):
#     if k == 0 or k > n:
#         print(f"Nhap lai k khac 0 va nho hon {n} !!!!")
#     else:
#         for i in range(1, n + 1, 1):
#             if i % k == 0:
#                 print(f"{i}", end=(","))
#         else:
#             print("Done!")
#
# List_div_k(45, 7)
# List_div_k(10, 2)
# List_div_k(100, 8)
# def tinh_Tong(a, b):
#     print("Tong la: ", a + b)
#
#
# def tinh_Hieu(a, b):
#     print("Hieu la: ", a - b)
#
#
# def tinh_Tich(a, b):
#     print("Tich la: ", a * b)
#
#
# def tinh_Thuong(a, b):
#     print("Thuong la: ", a / b)
#
#
# a = int(input("NHap a:"))
# b = int(input("Nhap b :"))
# print("___________________")
# tinh_Tong(a, b)
# print(f"Tong +10 la: {int(tinh_Tong(a, b)+10)}")
# tinh_Hieu(a, b)
# tinh_Tich(a, b)
# tinh_Thuong(a, b)
# def tinh(a,b):
#     print("Tong la: ",a+b)
#     print("Hieu la: ",a-b)
#     print("Tich la: ",a*b)
#     print("Thuong la:",a/b)
#
# a = int (input("NHap a:"))
# b = int (input("Nhap b :"))
# print("___________________")
# tinh(a,b)
# def info(first_name, mid_name, last_name ="", age = 20):
#     print(f"Thong tin la: {first_name} {mid_name} {last_name} {age}")
# info("Man","Thi","Lan",22)
# info("Man","Thi","Lan")
# info("Man","Lan")
# a = ["1","2","3","4",8]
# b=["hoa"]
# print("List_a: ",len(a))
# print(a[0]) #ptu dau tien ben trai
# print(a[-1]) #ptu dau tien ben phai
# print(a[0:3]) # start:stop
# print(a[-3:])
# a.append("lan")
# a[0:3] = ["6","7","9"]
# print(a)
# print(a+b)


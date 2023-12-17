
# n = int(input("Nhập n: "))
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j or i == n - 1 - j:
#             print("* ", end=" ")
#         else:
#             print("  ", end=" ")
#     print()

def tim_phan_tu_giong_nhau(mang1, mang2):
    phan_tu_giong_nhau = []

    for phan_tu in mang1:
        if phan_tu in mang2 and phan_tu not in phan_tu_giong_nhau:
            phan_tu_giong_nhau.append(phan_tu)

    return phan_tu_giong_nhau

# Nhập vào mảng thứ nhất
mang1 = input("Nhập vào mảng thứ nhất (các phần tử cách nhau bằng khoảng trắng): ").split()

# Nhập vào mảng thứ hai
mang2 = input("Nhập vào mảng thứ hai (các phần tử cách nhau bằng khoảng trắng): ").split()

# Chuyển đổi các phần tử thành số nguyên (nếu làm việc với số nguyên)
mang1 = [int(x) for x in mang1]
mang2 = [int(x) for x in mang2]

# Tìm và in ra các phần tử giống nhau
ket_qua = tim_phan_tu_giong_nhau(mang1, mang2)
if ket_qua:
    print("Các phần tử giống nhau là:", ket_qua)
else:
    print("Không có phần tử nào giống nhau.")
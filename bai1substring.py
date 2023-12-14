# Nhập hai mảng từ người dùng
A = list(map(int, input("Nhập các phần tử của mảng A, cách nhau bởi dấu cách: ").split()))
B = list(map(int, input("Nhập các phần tử của mảng B, cách nhau bởi dấu cách: ").split()))

# Hợp nhất hai mảng
C = A + B 

# Định nghĩa hàm dùng bubble sort để sort phần tử trong mảng tăng dần 
def bubble_sort_asc(C):
    n = len(C)
    for i in range(n):
        for j in range(0, n - i - 1):
            if C[j] > C[j + 1]:
                # Hoán đổi C[j] và C[j + 1]
                C[j], C[j + 1] = C[j + 1], C[j]
    return C

# Thực thi sắp xếp mảng C bằng bubble sort
C = bubble_sort_asc(C)

# Tính giá trị trung vị bằng cách check số chẵn số lẻ
if len(C) % 2 == 0:
    median = (C[len(C) // 2] + C[len(C) // 2 - 1]) / 2
else:
    median = C[len(C) // 2]
c
# In kết quả
print("Mảng sau khi đã hợp nhất và sắp xếp: ", C)
print("Giá trị trung vị của mảng: ", median)

#bài1

def lengthOfLongestSubstring(s):
    k = 0
    maxLength = 0
    for i in range(len(s)):
        for j in range(k, i):
            if s[i] == s[j]:
                k = j + 1
                break
        if i - k + 1 > maxLength:
            maxLength = i - k + 1
    return maxLength

n = input("nhap mot chuoi: ")
check = lengthOfLongestSubstring(n)
print(check)

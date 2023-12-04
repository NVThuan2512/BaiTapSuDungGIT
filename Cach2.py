#Cách 2
#khởi tạo hàm twoSum với 2 parameter là nums và target
def twoSum(nums, target):
    #chạy vòng lặp các phần tử trong mảng
    for i in range(len(nums)):
        #chạy vòng lặp các phần tử trong mảng bắt đầu từ giá trị thứ 2 trong mảng
        for j in range(i+1, len(nums)):
            #kiểm tra sau 2 vòng lặp, nếu như giá trị đầu tiên trong mảng + giá trị kế bên( ví dụ như [0] = 3 và [1] = 2 cộng nhau
            #mà = 6 thì trả về vị trí 2 đứa đó
            if nums[i] + nums[j] == target:
                return [i, j]
    return None
print(twoSum([3, 2, 4], 6))
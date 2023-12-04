#cách giải số 1
def twoSum(nums, target):
    #khởi tạo dict
    num_dict = {}
    #khởi tạo vòng lặp với tham số đầu vào là nums với enumerate trả về mỗi phần tử cùng chỉ số của nó
    for i, num in enumerate(nums):
        #kiểm tra xem số target - num có nằm trong mảng num_dict không?
        if target - num in num_dict:
            #với số đầu vào là 2, ta kiểm tra xem 9(số target) - 2 = 7 có nằm trong mảng không
            #nếu có ta sẽ trả về số 7 và đồng thời vị trí của nó trong mảng
            return [num_dict[target - num], i]
        #gán giá trị bằng vị trí
        num_dict[num] = i
    #nếu không có sẽ trả về none
    return None
print(twoSum([2, 7, 11, 15], 9))
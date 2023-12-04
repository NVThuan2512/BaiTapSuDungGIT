#Cách 3
#khởi tạo hàm twoSum với 2 parameter là nums và target
def twoSum(nums, target):
    num_dict = {num: i for i, num in enumerate(nums)}
    # Đây là vòng lặp for duyệt qua mỗi phần tử num trong danh sách nums. enumerate(nums) 
    #trả về cả chỉ số i và giá trị num tại chỉ số đó
    for i, num in enumerate(nums):
    #Kiểm tra xem target - num có tồn tại trong từ điển num_dict hay không. Trong trường hợp này, target là 6 và num là 3 (phần tử đầu tiên trong mảng), 
    #vì vậy target - num cũng là 3. Vì 3 có trong num_dict (vì nó là phần tử thứ hai trong mảng), điều kiện này trả về True   
    ##    
    #Kiểm tra xem chỉ số hiện tại i có khác với chỉ số của target - num trong num_dict hay không. Điều này đảm bảo rằng ta không sử dụng cùng
    #một phần tử hai lần. Trong trường hợp này, i là 0 (chỉ số của phần tử đầu tiên) và num_dict[target - num] là 1 (chỉ số của phần tử thứ hai, tức là 3), 
    #vì vậy điều kiện này cũng trả về True
        if target - num in num_dict and i != num_dict[target - num]:
            return [i, num_dict[target - num]]
    return None
print(twoSum([3, 3], 6))
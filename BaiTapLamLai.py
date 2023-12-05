def hamkiemtrasodoixung(n):
    # flag = 1 trường hợp số sẽ đối xứng
    # flag = 0 trường hợp số không đối xứng
    #ban đầu ta gán flag = 0 rồi mới kiếm tra điều kiện
    flag = 0;
    #Trong Python, n[::-1] là cú pháp để lấy một chuỗi đảo ngược của n. Cụ thể, : đầu tiên đại diện cho vị trí bắt đầu cắt chuỗi (ở đây không xác định nên sẽ lấy từ đầu),
    # : thứ hai đại diện cho vị trí kết thúc cắt chuỗi (ở đây không xác định nên sẽ lấy đến cuối), và -1 sau cùng đại diện cho bước nhảy khi cắt chuỗi.
    # Trong trường hợp này, bước nhảy là -1, nghĩa là nó sẽ bắt đầu từ cuối chuỗi và đi ngược lại về đầu chuỗi, tạo ra một chuỗi đảo ngược.
    #Vì vậy, n[::-1] sẽ tạo ra một chuỗi mới là chuỗi đảo ngược của n.
    #Cuối cùng, n[::-1] == n sẽ so sánh chuỗi đảo ngược vừa tạo với chuỗi gốc.
    #Nếu chúng giống nhau, điều kiện này sẽ trả về True, tức là n là một chuỗi đối xứng.
    #Ngược lại, nếu chúng không giống nhau, điều kiện này sẽ trả về False, tức là n không phải là chuỗi đối xứng.
    #Ví dụ như người dùng nhập 19891, ta sẽ đi từ cuối chuỗi tới với giá trị nhảy là -1. Trong số input 19891 có 5 số, ta bắt đầu từ số cuối cùng là số 4 vì
    #0 1 2 3 4 = 5 - 1  đi từ cuối chuỗi đến đầu chuỗi, tạo ra một chuỗi đảo ngược và sau đó so sánh xem nó có bằng số input không, nếu bằng thì flag = 1 là số đối xứng
    #Không bằng thì flag = 0 là không đối xứng

    if (n[::-1] == n):
        flag = 1
    return flag


n = input(">> nhap mot so tu nhien: ")
check = hamkiemtrasodoixung(n);

if check == 1:
    print(n, "la so doi xung")
else:
    print(n, "khong phai la so doi xung")

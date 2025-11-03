
# x = 10
# y = "Hello"

# print(f"Giá trị của x: {x}")
# print(f"Địa chỉ của đối tượng mà biến x trỏ tới: {id(x)}")
# print(f"Kiểu của đối tượng: {type(x)}")

# print(f"Giá trị của y: {y}")
# print(f"Địa chỉ của đối tượng mà biến y trỏ tới: {id(y)}")
# print(f"Kiểu của đối tượng: {type(y)}")

# #* Phép gán tham chiếu (Aliasing)

# a = [1, 2, 3]  #* List kiểu dữ liệu khả biến

# b = a

# print(f"Giá trị của a: {a}")
# print(f"ID của a: {id(a)}")

# print(f"Giá trị của b: {b}")
# print(f"ID của b: {id(b)}")

# #* SO SÁNH ID
# print(f"a và b có trỏ đến cùng 1 đối tượng không? {a is b}")


# print("CHANGE")

# #* Thay đổi đối tượng qua TÊN 'b'
# b.append(5)
# print(f"Giá trị của b bây giờ: {b}")
# #* Kiểm tra a
# print(f"Giá trị của a là: {a}")

# print(f"ID của a: {id(a)}")
# print(f"ID của b: {id(b)}")


# x = 100
# y = x

# print(x)
# print(y)

# print(f"ID của x: {id(x)}")
# print(f"ID của y: {id(y)}")

# x = x + 1

# print(f"Giá trị mới: {x}")
# print(f"ID hiện tại: {id(x)}")

# print(f"Giá trị y hiện tại: {y}")
# print(f"ID y hiện tại: {id(y)}")

#* Truyền tham số vào FUNCTION

#* Ví dụ 5

#* Hàm thay đổi đối tượng KHẢ BIẾN 
def modify_list(lst):
    print(f"Bên trong hàm - ID của lst: {id(lst)}")
    lst.append(100)
    print(f"lst đã thay đổi: {lst}")

#* Hàm gán lại tham số (BẤT BIẾN)

def try_to_change_number(num):
    print(f"ID của num: {id(num)}")
    num = num + 10
    print(num)
    print(f"ID mới của num: {id(num)}")


my_list = [1, 2]
print(f"[Bên ngoài hàm] ID của my_list (trước khi gọi hàm): {id(my_list)}")
print(my_list)
modify_list(my_list) #* Truyền tham chiếu đến my_list
print(f"[Bên ngoài hàm] ID của my_list (sau khi gọi hàm): {id(my_list)}")

#***
my_number = 5
print(f"[Bên ngoài hàm] ID của my_number (trước khi gọi hàm): {id(my_number)}")
print(my_number)
try_to_change_number(my_number)
print(f"[Bên ngoài hàm] ID của my_number (sau khi gọi hàm): {id(my_number)}")
print(my_number)

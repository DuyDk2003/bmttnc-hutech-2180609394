def tao_tuple_tu_list(lst):
    return tuple(lst)

intput_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")

numbers = list(map(int,intput_list.split(',')))

my_tuple = tao_tuple_tu_list(numbers)
print("List: ",numbers)
print("Tuple từ List: ",my_tuple)
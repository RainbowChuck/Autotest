int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
int_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_int_list = [int_list[i] + int_list1[i] for i in range(len(int_list))]
print(sum_int_list)
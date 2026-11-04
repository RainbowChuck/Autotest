
def sum_lists(int_list1, int_list2):
    if len(int_list1) == len(int_list2):
        sum_int_list = [int_list1[i] + int_list2[i] for i in range(len(max(int_list1,int_list2,key=len)))]
    else:
        min_len = min(int_list1, int_list2, key=len)
        max_len = max(int_list1, int_list2, key=len)
        sum_int_list = [int_list1[i] + int_list2[i] for i in range(len(min_len))]
        for i in range(len(min_len), len(max_len)):
            sum_int_list.append(max_len[i])

    return sum_int_list


int_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
int_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
int_list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_lists(int_list1, int_list2))
print(sum_lists(int_list3, int_list2))
print(sum_lists(int_list2, int_list1))

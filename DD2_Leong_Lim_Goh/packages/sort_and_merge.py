'''
@authors:
    Leong Jing Wen
    Lim Yu Jie
    Lisa Shannon Goh
NTU BCG Y1S1 2018-19
'''

# merge function for merge_sort
def merge(left_list, right_list):
    result_list = []

    while left_list and right_list:
        if left_list[0] < right_list[0]:
            result_list.append(left_list[0])
            left_list.pop(0)
        else:
            result_list.append(right_list[0])
            right_list.pop(0)

    if left_list:
        result_list.extend(left_list)
    else:
        result_list.extend(right_list)
        
    return result_list
        

# merge sort function for sorting data
def merge_sort(list_of_items):
    list_len = len(list_of_items)
    
    if list_len < 2:
        return list_of_items
    left_list = list_of_items[:list_len // 2]
    right_list = list_of_items[list_len // 2:]
    
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return merge(left_list, right_list)


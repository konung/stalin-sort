def sort(list):
    sorted_list = [list[0]]
    for e in list[1:]:
        if e >= sorted_list[-1]:
            sorted_list.append(e)
    return sorted_list

ordered_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sorted_list = sort(ordered_list)
print("Original: {0}\nSorted: {1}\n".format(ordered_list, sorted_list))

reversed_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
sorted_list = sort(reversed_list)
print("Original: {0}\nSorted: {1}\n".format(reversed_list, sorted_list))

mixed_list = [1, 3, 2, 5, 4, 7, 6, 9, 8]
sorted_list = sort(mixed_list)
print("Original: {0}\nSorted: {1}\n".format(mixed_list, sorted_list))

test_list = [1,5,2,4]
sorted_list = sort(test_list)
print("Original: {0}\nSorted: {1}\n".format(test_list, sorted_list))


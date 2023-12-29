def count_sort(data):
    count_list = [0 for i in range(10)]
    for i in range(len(data)):
        count_list[data[i]] = count_list[data[i]] + 1
    return count_list

data = [9, 4, 5, 2, 8, 3, 7, 8, 3, 2, 6, 5, 7, 9, 2, 9]
print(count_sort(data))
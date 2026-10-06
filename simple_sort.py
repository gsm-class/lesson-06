def insertion_sort(num_list):
    bef_s_list = num_list.copy()

    # pass

    return bef_s_list

def selection_sort(num_list):
    bef_s_list = num_list.copy()

    # pass

    return bef_s_list

def bubble_sort(num_list):
    bef_n_list = num_list.copy()

    # pass

    return bef_n_list

n = int(input())
num_list = []

for _ in range(n):
    num = int(input())
    num_list.append(num)

insertion_sorted_list = insertion_sort(num_list)
print(" ".join(map(str, insertion_sorted_list)))

selection_sorted_list = selection_sort(num_list)
print(" ".join(map(str, selection_sorted_list)))

bubble_sorted_list = bubble_sort(num_list)
print(" ".join(map(str, bubble_sorted_list)))

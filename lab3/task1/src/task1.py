import utils
import os
import random

def partition(a, l, r):
    """"Разбиение для обычной сортировки"""
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j = j + 1
            a[j], a[i] = a[i], a[j]
    a[l], a[j] = a[j], a[l]
    return j

def randomized_quick_sort(a, l, r):
    """"Обычная быстрая сортировка"""
    if l < r:
        k = random.randint(l, r)
        a[l], a[k] = a[k], a[l]
        m = partition(a, l, r)
        randomized_quick_sort(a, l, m - 1)
        randomized_quick_sort(a, m + 1, r)



def randomized_quick_sort_best(a, l, r):
    """Улучшенная версия быстрой сортировки"""
    if l < r:
        k = random.randint(l, r)
        a[l], a[k] = a[k], a[l]
        m1, m2 = partition_best(a, l, r)
        randomized_quick_sort_best(a, l, m1 - 1)
        randomized_quick_sort_best(a, m2 + 1, r)
    return  a

def partition_best(a, l, r):
    """Трёхстороннее разделение"""
    x = a[l]
    m1 = l
    m2 = l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            m1 += 1
            a[m1], a[i] = a[i], a[m1]
            if m1 != m2:
                m2 += 1
                a[m2], a[m1] = a[m1], a[m2]
        elif a[i] == x:
            m2 += 1
            a[m2], a[i] = a[i], a[m2]
    a[l], a[m1] = a[m1], a[l]
    return m1, m2

if __name__ == '__main__':
    print("Lab 3 Task 1:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str).split()
    n = data[0]
    arr = data[1:]
    result = randomized_quick_sort_best(arr, 0, len(arr)-1)

    print(f"Input: {data}")
    print(f"Output: {result}")

    utils.write_in_file(output_path, result)
    utils.print_time_memory(time_start)
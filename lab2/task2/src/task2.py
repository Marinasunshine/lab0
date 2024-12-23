import utils
import os

def merge(a, l, r, l_start, r_end):
    res = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1

    while i < len(l):
        res.append(l[i])
        i += 1

    while j < len(r):
        res.append(r[j])
        j += 1

    a[l_start:r_end + 1] = res
    return a

def merge_sort(a, l, r):
    if l < r:
        mid = (l + r) // 2
        merge_sort(a, l, mid)
        merge_sort(a, mid + 1, r)
        merge(a, a[l:mid + 1], a[mid + 1:r + 1], l, r)
    return a

if __name__ == "__main__":
    print("Lab 2 Task 2:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path)
    n = int(data[0])
    a = list(map(int, data[1:]))

    result = merge_sort(a, 0, len(a) - 1)

    print(f"Input: {data}")
    print(f"Output: {result}")

    utils.write_in_file(output_path, result)
    utils.print_time_memory(time_start)
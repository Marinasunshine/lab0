import utils
import os

def merge(l, r):
    res = []
    i = j = inversions = 0

    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            inversions += len(l) - i
            j += 1

    res.extend(l[i:])
    res.extend(r[j:])

    return res, inversions


def merge_sort(a):
    if len(a) <= 1:
        return a, 0

    mid = len(a) // 2
    l, l_inversions = merge_sort(a[:mid])
    r, r_inversions = merge_sort(a[mid:])
    merged, split_inv = merge(l, r)

    return merged, l_inversions + r_inversions + split_inv

if __name__ == "__main__":
    print("Lab 2 Task 3:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path)
    n = data[0]
    a = data[1:]
    sort, result = merge_sort(a)

    print(f"Input: {data}")
    print(f"Output: {result}")

    utils.write_in_file(output_path, str(result))
    utils.print_time_memory(time_start)
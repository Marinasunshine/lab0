import utils
import os
import sys

sys.setrecursionlimit(50000)
def insertion_sort(arr, n):
    if n <= 1:
        return
    insertion_sort(arr, n - 1)
    key = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] < key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

if __name__ == '__main__':
    print("Lab 1 Task 3:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path)
    n = data[0]
    a = data[1:]

    insertion_sort(a, n)

    print(f"Input: {data}")
    print(f"Output: {a}")

    utils.write_in_file(output_path, a)
    utils.print_time_memory(time_start)
import utils
import os

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr

if __name__ == '__main__':
    print("Lab 1 Task 6:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path)
    n = data[0]
    a = data[1:]

    bubble_sort(a)

    print(f"Input: {data}")
    print(f"Output: {a}")

    utils.write_in_file(output_path, a)
    utils.print_time_memory(time_start)

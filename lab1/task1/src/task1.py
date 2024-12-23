import utils
import os

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == '__main__':
    print("Lab 1 Task 1:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path)
    a = data[1:]
    n = data[0]

    insertion_sort(a)

    print(f"Input: {data}")
    print(f"Output: {a}")

    utils.write_in_file(output_path, a)
    utils.print_time_memory(time_start)

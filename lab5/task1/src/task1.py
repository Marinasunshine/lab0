import utils
import os

def check_heap(arr):
    n = len(arr)
    for i in range(1, n + 1):
        left = 2 * i
        right = 2 * i + 1
        if left <= n and arr[i - 1] > arr[left - 1]:
            return "NO"
        if right <= n and arr[i - 1] > arr[right - 1]:
            return "NO"
    return "YES"

if __name__ == '__main__':
    print("Lab 5 Task 1:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str)
    data = data.split()
    data = list(map(int, data[1:]))
    result = check_heap(data)

    print(f"Input: {data}")
    print(f"Output: {result}")

    utils.write_in_file(output_path, result)
    utils.print_time_memory(time_start)

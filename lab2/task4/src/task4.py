import utils
import os

def binary_search(a, target):
    l = 0
    r = len(a) - 1

    while l <= r:
        mid = (l + r) // 2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return -1

if __name__ == "__main__":
    print("Lab 2 Task 4:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path)
    n = int(data[0])
    a = list(map(int, data[1:n + 1]))
    k = int(data[n + 1])
    b = list(map(int, data[n + 2:]))
    result = [binary_search(a, number) for number in b]

    print(f"Input: {data}")
    print(f"Output: {result}")

    utils.write_in_file(output_path, result)
    utils.print_time_memory(time_start)
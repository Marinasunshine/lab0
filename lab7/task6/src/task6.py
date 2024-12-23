import utils
import os

def longest_lengths(arr):
    n = len(arr)
    lengths = [1] * n
    prev = [-1] * n
    max_len = 1
    max_index = 0

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                prev[i] = j
                if lengths[i] > max_len:
                    max_len = lengths[i]
                    max_index = i

    l = []
    index = max_index
    while index != -1:
        l.append(arr[index])
        index = prev[index]
    l.reverse()

    return max_len, l

if __name__ == '__main__':
    print("Lab 7 Task 6:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str)
    data = data.split()
    data = list(map(int, data))

    result = longest_lengths(data[1:])

    print(f"Input: {data}")
    print(f"Output: {result}")

    utils.write_in_file(output_path, result, split_str="\n")
    utils.print_time_memory(time_start)
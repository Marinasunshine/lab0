import utils
import os

def lin_search(arr, V):
    ind = []
    for i in range(len(arr)):
        if arr[i] == V:
            ind.append(i)
    if ind:
        return len(ind), ind
    else:
        return -1

if __name__ == '__main__':
    print("Lab 1 Task 4:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path)
    a = data[:-1]
    v = data[-1]

    result = lin_search(a, v)

    print(f"Input: {data}")
    print(f"Output: {result}")

    utils.write_in_file(output_path, result)
    utils.print_time_memory(time_start)

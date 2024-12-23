import utils
import os

def scarecrow_sort(n, k, matr):
    groups = [[] for i in range(k)]
    for i in range(n):
        groups[i % k].append(matr[i])
    for group in groups:
        group.sort()
    sorted_matr = [groups[i % k][i // k] for i in range(n)]
    return "ДА" if sorted_matr == sorted(matr) else "НЕТ"

if __name__ == "__main__":
    print("Lab 3 Task 3:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path)
    n = data[0]
    k = data[1]
    arr = data[2:]
    result = scarecrow_sort(n, k, arr)

    print(f"Input: {data}")
    print(f"Output: {result}")

    utils.write_in_file(output_path, result)
    utils.print_time_memory(time_start)

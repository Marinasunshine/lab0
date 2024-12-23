import utils
import os

def binary_numbers(a, b):
    a = [int(x) for x in a]
    b = [int(x) for x in b]
    n = max(len(a), len(b))
    a = [0] * (n - len(a)) + a
    b = [0] * (n - len(b)) + b
    c = [0] * (n + 1)
    carry = 0
    for i in range(n - 1, -1, -1):
        total = a[i] + b[i] + carry
        c[i + 1] = total % 2
        carry = total // 2
    c[0] = carry

    return c

if __name__ == '__main__':
    print("Lab 1 Task 4:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path)
    a = str(data[0]).strip()
    b = str(data[1]).strip()

    c = binary_numbers(a, b)

    print(f"Input: {data}")
    print(f"Output: {''.join(map(str, c))}")

    utils.write_in_file(output_path, [''.join(map(str, c))])
    utils.print_time_memory(time_start)
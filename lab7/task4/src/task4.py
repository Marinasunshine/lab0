import utils
import os

def length(a, b):
    len1 = len(a)
    len2 = len(b)
    prev_row = [0] * (len2 + 1)
    curr_row = [0] * (len2 + 1)

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if a[i - 1] == b[j - 1]:
                curr_row[j] = prev_row[j - 1] + 1
            else:
                curr_row[j] = max(prev_row[j], curr_row[j - 1])
        prev_row, curr_row = curr_row, [0] * (len2 + 1)

    return prev_row[len2]

if __name__ == '__main__':
    print("Lab 7 Task 4:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str)
    data = data.splitlines()
    seq1 = list(map(int, data[1].split()))
    seq2 = list(map(int, data[3].split()))

    result = length(seq1, seq2)

    print(f"Input: {data}")
    print(f"Output: {result}")

    utils.write_in_file(output_path, [result], split_str="\n")
    utils.print_time_memory(time_start)
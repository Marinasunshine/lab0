import utils
import os

def is_match(pattern, s):
    m = len(pattern)
    n = len(s)
    match = [[False] * (n + 1) for i in range(m + 1)]
    match[0][0] = True

    for i in range(1, m + 1):
        if pattern[i - 1] == '*':
            match[i][0] = match[i - 1][0]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[i - 1] == '*':
                match[i][j] = match[i - 1][j] or match[i][j - 1]
            elif pattern[i - 1] == '?' or pattern[i - 1] == s[j - 1]:
                match[i][j] = match[i - 1][j - 1]

    if match[m][n]:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    print("Lab 7 Task 7:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str)
    data = data.split('\n')

    result = is_match(data[0], data[1])

    print(f"Input: {data}")
    print(f"Output: {result}")

    utils.write_in_file(output_path, [result], split_str="\n")
    utils.print_time_memory(time_start)
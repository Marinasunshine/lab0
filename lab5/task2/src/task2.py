import utils
import os

def find_height(parents, n):
    children = [[] for _ in range(n)]
    root = -1
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            children[parents[i]].append(i)
    stack = [(root, 1)]
    max_height = 0
    while stack:
        node, height = stack.pop()
        max_height = max(max_height, height)
        for child in children[node]:
            stack.append((child, height + 1))

    return max_height

if __name__ == '__main__':
    print("Lab 5 Task 2:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str)
    data = data.split()
    data = list(map(int, data))
    result = find_height(data[1:], data[0])

    print(f"Input: {data}")
    print(f"Output: {result}")

    utils.write_in_file(output_path, str(result), split_str="\n")
    utils.print_time_memory(time_start)


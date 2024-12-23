import utils
import os

def brackets(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for i, element in enumerate(s):
        if element in '([{':
            stack.append((element, i + 1))
        elif element in ')]}':
            if not stack:
                return i + 1
            top, index = stack.pop()
            if top != pairs[element]:
                return i + 1
    if stack:
        return stack[-1][1]

    return "Success"

if __name__ == '__main__':
    print("Lab 4 Task 4:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str)
    data = data.split("\n")
    result = brackets(data)

    print(f"Input: {data}")
    print(f"Output: {result}")

    utils.write_in_file(output_path, str(result))
    utils.print_time_memory(time_start)
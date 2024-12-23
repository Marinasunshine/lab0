import utils
import os

def stack_max(commands):
    stack = []
    max_stack = []
    result = []

    for command in commands:
        if command[0] == 'push':
            value = int(command[1])
            stack.append(value)
            if not max_stack or value >= max_stack[-1]:
                max_stack.append(value)
        elif command[0] == 'pop':
            if stack:
                value = stack.pop()
                if value == max_stack[-1]:
                    max_stack.pop()
        elif command[0] == 'max':
            if max_stack:
                result.append(str(max_stack[-1]))

    return result

if __name__ == '__main__':
    print("Lab 4 Task 5:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str)
    data = data.split("\n")
    commands = [line.split() for line in data[1:]]
    result = stack_max(commands)

    print(f"Input: {data}")
    print(f"Output: {result}")

    utils.write_in_file(output_path, result, split_str="\n")
    utils.print_time_memory(time_start)
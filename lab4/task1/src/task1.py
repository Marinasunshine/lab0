import utils
import os

def stacks(commands):
    stack = []
    result = []

    for command in commands:
        if command[0] == '+':
            stack.append(int(command.split()[1]))
        elif command == '-':
            result.append(stack.pop())

    return result

if __name__ == '__main__':
    print("Lab 4 Task 1:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str)
    data = data.split("\n")
    result = stacks(data[1:])

    print(f"Input: {data}")
    print(f"Output: {result}")

    utils.write_in_file(output_path, result, split_str="\n")
    utils.print_time_memory(time_start)
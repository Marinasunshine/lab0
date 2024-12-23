import utils
import os

def set_operations(commands):
    s = set()
    result = []

    for command in commands:
        action = command[0]
        value = int(command.split()[1])

        if action == 'A':
            s.add(value)
        elif action == 'D':
            s.discard(value)
        elif action == '?':
            result.append("Y" if value in s else "N")

    return result

if __name__ == '__main__':
    print("Lab 6 Task 1:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str)
    data = data.split("\n")
    result = set_operations(data[1:])

    print(f"Input: {data}")
    print(f"Output: {result}")

    utils.write_in_file(output_path, result, split_str="\n")
    utils.print_time_memory(time_start)
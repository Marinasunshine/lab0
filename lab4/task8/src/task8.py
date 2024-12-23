import utils
import os

def postfix(data):
    stack = []

    for element in data:
        if element.isdigit() or (element[0] == '-' and len(element) > 1):
            stack.append(int(element))
        else:
            b = stack.pop()
            a = stack.pop()
            if element == '+':
                stack.append(a + b)
            elif element == '-':
                stack.append(a - b)
            elif element == '*':
                stack.append(a * b)

    return stack[0]

if __name__ == '__main__':
    print("Lab 4 Task 8:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str)
    data = data.split()
    data = list(map(str, data[1:]))
    result = postfix(data)

    print(f"Input: {data}")
    print(f"Output: {result}")

    utils.write_in_file(output_path, str(result))
    utils.print_time_memory(time_start)
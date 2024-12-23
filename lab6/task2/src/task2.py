import utils
import os

def phonebook_manager(numbers):
    phonebook = {}
    results = []

    for num in numbers:
        part = num.split()
        command = part[0]
        if command == 'add':
            number, name = part[1], part[2]
            phonebook[number] = name
        elif command == 'del':
            number = part[1]
            phonebook.pop(number, None)
        elif command == 'find':
            number = part[1]
            results.append(phonebook.get(number, 'not found'))

    return results

if __name__ == '__main__':
    print("Lab 6 Task 2:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str)
    data = data.split("\n")
    result = phonebook_manager(data[1:])

    print(f"Input: {data}")
    print(f"Output: {result}")

    utils.write_in_file(output_path, result, split_str="\n")
    utils.print_time_memory(time_start)
import utils
import os

def generate_worst_case(n):
    n = int(n)
    return list(range(n, 0, -1))

if __name__ == "__main__":
    print("Lab 3 Task 2:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path)
    data = data[0]
    result = generate_worst_case(data)

    print(f"Input: {data}")
    print(f"Output: {result}")

    utils.write_in_file(output_path, result)
    utils.print_time_memory(time_start)
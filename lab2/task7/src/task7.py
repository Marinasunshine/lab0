import utils
import os

def max_sub(a):
    max_sum = curr_sum = a[0]
    start = end = temp_start = 0

    for i in range(1, len(a)):
        if curr_sum + a[i] < a[i]:
            curr_sum = a[i]
            temp_start = i
        else:
            curr_sum += a[i]

        if curr_sum > max_sum:
            max_sum = curr_sum
            start = temp_start
            end = i

    return a[start:end + 1]

if __name__ == "__main__":
    print("Lab 2 Task 7:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path)
    arr = data[1:]
    result = max_sub(arr)

    print(f"Input: {data}")
    print(f"Output: {result}")

    utils.write_in_file(output_path, result)
    utils.print_time_memory(time_start)
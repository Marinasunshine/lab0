import utils
import os

def h_index(citations):
    """Вычисление индекса Хирша"""
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] < i + 1:
            return i
    return len(citations)

if __name__ == "__main__":
    print("Lab 3 Task 5:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path)
    arr = data
    result = h_index(arr)

    print(f"Input: {data}")
    print(f"Output: {result}")

    utils.write_in_file(output_path, str(result))
    utils.print_time_memory(time_start)
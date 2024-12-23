import utils
import os

def find_max(n, arr, m):
    dequeue = []
    result = []

    for i in range(n):
        if dequeue and dequeue[0] < i - m + 1:
            dequeue.pop(0)
        while dequeue and arr[dequeue[-1]] < arr[i]:
            dequeue.pop()
        dequeue.append(i)
        if i >= m - 1:
            result.append(arr[dequeue[0]])

    return result

if __name__ == '__main__':
    print("Lab 4 Task 7:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str).split("\n")
    n = int(data[0])
    arr = list(map(int, data[1].split()))
    m = int(data[-1])
    result = find_max(n, arr, m)

    print(f"Input: {data}")
    print(f"Output: {result}")

    utils.write_in_file(output_path, result)
    utils.print_time_memory(time_start)
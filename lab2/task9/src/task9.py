import utils
import os

def matrix_mult(n, X, Y):
    Z = [[0] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                Z[i][j] += X[i][k] * Y[k][j]

    return Z

if __name__ == "__main__":
    print("Lab 2 Task 9:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path)
    n = data[0]
    data = data[1:]
    A = [data[i:i + n] for i in range(0, n * n, n)]
    B = [data[i:i + n] for i in range(n * n, 2 * n * n, n)]
    result = matrix_mult(n, A, B)

    print(f"Input: {data}")
    print(f"Output: {result}")

    utils.write_in_file(output_path, result)
    utils.print_time_memory(time_start)
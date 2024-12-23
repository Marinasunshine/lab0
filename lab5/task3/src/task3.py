import utils
import os

def process_packets(S, packets):
    finish_time = []
    result = []

    for Ai, Pi in packets:
        finish_time = [t for t in finish_time if t > Ai]
        if len(finish_time) >= S:
            result.append(-1)
        else:
            if not finish_time:
                start_time = Ai
            else:
                start_time = finish_time[-1]

            finish_time.append(start_time + Pi)
            result.append(start_time)

    return result

if __name__ == '__main__':
    print("Lab 5 Task 3:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str).strip().split('\n')
    S, _ = map(int, data[0].split())
    packets = [tuple(map(int, line.split())) for line in data[2:] if line.strip()]
    result = process_packets(S, packets)

    print(f"Input: {data}")
    print(f"Output: {result}")

    utils.write_in_file(output_path, result, split_str="\n")
    utils.print_time_memory(time_start)
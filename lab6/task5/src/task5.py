import utils
import os

def vote(data):
    votes = {}
    for line in data:
        candidate, vote_count = line.split()
        vote_count = int(vote_count)
        if candidate in votes:
            votes[candidate] += vote_count
        else:
            votes[candidate] = vote_count
    sorted_candidates = sorted(votes.items())

    return [f"{candidate} {count}" for candidate, count in sorted_candidates]

if __name__ == '__main__':
    print("Lab 6 Task 5:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str)
    data = data.split("\n")
    result = vote(data)

    print(f"Input: {data}")
    print(f"Output: {result}")

    utils.write_in_file(output_path, result, split_str="\n")
    utils.print_time_memory(time_start)
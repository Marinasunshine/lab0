import utils
import os

def min_coins(money, coins):
    min_coins = [float('inf')] * (money + 1)
    min_coins[0] = 0

    for i in range(1, money + 1):
        for coin in coins:
            if i >= coin:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    if min_coins[money] == float('inf'):
        return -1
    else:
        return min_coins[money]

if __name__ == '__main__':
    print("Lab 7 Task 1:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type=str)
    data = data.split()
    data = list(map(int, data))

    result = min_coins(data[0], data[2:])

    print(f"Input: {data}")
    print(f"Output: {result}")

    utils.write_in_file(output_path, [result], split_str="\n")
    utils.print_time_memory(time_start)
import utils
import os

def palindrome(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    left_half = []
    middle_char = ''

    for char in sorted(freq.keys()):
        count = freq[char]
        pair_count = count // 2
        left_half.append(char * pair_count)
        if count % 2 == 1 and middle_char == '':
            middle_char = char

    left_half_str = ''.join(left_half)
    palindrome = left_half_str + middle_char + left_half_str[::-1]

    return palindrome

if __name__ == '__main__':
    print("Lab 1 Task 10:")
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

    data = utils.read_from_file(input_path, type = str)
    a = data
    result = palindrome(a)

    print(f"Input: {data}")
    print(f"Output: {result}")

    utils.write_in_file(output_path, [result])
    utils.print_time_memory(time_start)
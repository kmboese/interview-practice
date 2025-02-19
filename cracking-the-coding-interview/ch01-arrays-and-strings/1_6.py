'''
String compression: implement a method to perform basic string compression using
the counts of repeated characters.

Example: string "aabccccaaa" would become "a2b1c5a3". 

If the compressed string is not shorter than the original string, return the original 
string. Otherwise, return the compressed string.
'''

def get_compressed_string(input_string):
    count = 0
    previous_char = input_string[0]
    compressed_string = ""
    for index in range(len(input_string)):
        char = input_string[index]
        if char == previous_char:
            count += 1
        else:
            compressed_string += previous_char + str(count)
            count = 1
        previous_char = input_string[index]
    compressed_string += previous_char + str(count)

    if len(compressed_string) < len(input_string):
        return compressed_string
    else:
        return input_string


def run_tests():
    pairs = [
        ("aaaaaaaaaaaaaab", "a14b1"),
        ("abcd", "abcd"),
        ("abcdd", "abcdd"),
        ("adddd", "a1d4"),
        ("aabccccaaa", "a2b1c4a3")
    ]
    for pair in pairs:
        result = get_compressed_string(pair[0])
        print_result(pair[0], result)
        assert(result == pair[1])

def print_result(input_string, expected_string):
    print(f'Input: "{input_string}", output: "{get_compressed_string(expected_string)}"')

def main():
    run_tests()

if __name__ == '__main__':
    main()
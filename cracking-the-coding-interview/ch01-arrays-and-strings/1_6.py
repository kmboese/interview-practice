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
        

def main():
    # test_string = "aabccccaaa"
    test_string = "aaabb"
    compressed_string = get_compressed_string(test_string)
    print(f'Test string "{test_string}" compressed is "{compressed_string}"')

if __name__ == '__main__':
    main()
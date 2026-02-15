'''
Palindrome permutation: given a string, write a fn to check if it is a permutation
of a palindrome. The palindrome does not need to be a valid English word.

Example:
Input: Tact Coa
Ouptut: True (permutations: "taco cat", "atco acta", etc.)
'''

def get_character_frequencies(input_string):
    freqMap = {}
    for char in input_string:
        if freqMap.get(char):
            freqMap[char] += 1
        else:
            freqMap[char] = 1

    print(f'Debug: freqMap = {freqMap}')
    return freqMap

def is_palindrome_permutation(input_string):
    stripped_input = input_string.replace(" ", "")
    freqMap = get_character_frequencies(stripped_input)

    # special case: if all letters are the same, by definition it is a palindrome
    if len(freqMap.values()) == 1:
        return True

    if len(stripped_input) % 2 == 0:
        for value in freqMap.values():
            if value % 2 != 0:
                return False
        return True
    # String length is odd
    else:
        unique_letter_found = False
        for value in freqMap.values():
            if value == 1:
                if not unique_letter_found:
                    unique_letter_found = True
                else:
                    return False
            elif value % 2 != 0:
                return False
        return True
        
def run_tests():
    tests = [
        ("tact coa", True),
        ("bolton notlob", True),
        ("aaaa", True),
        ("aaa", True),
        ("madam im adam", True),
        ("kevin", False),
    ]
    
    for test in tests:
        print(f'Testing string: "{test[0]}"')
        assert is_palindrome_permutation(test[0]) == test[1]

def main():
    input_string = "taco cat"
    output = is_palindrome_permutation(input_string)
    print(f'Input string "{input_string}" is a palindrome permutation? -> {output}')
    run_tests()

if __name__ == '__main__':
    main()
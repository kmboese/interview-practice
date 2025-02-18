'''
Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
'''

# Simple solution with hashmap
def is_unique_string(string: str):
    characterMap = {}
    for char in string:
        if characterMap.get(char):
            return False
        else:
            characterMap[char] = 1
    return True

def run_tests():
    assert is_unique_string("abcdefghijklmnopqrstuvwxyz")
    assert is_unique_string("kevin")
    assert not is_unique_string("hello")

def main():
    run_tests()

if __name__ == '__main__':
    main()
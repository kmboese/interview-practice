'''
Given two strings, write a method to decide if one is a permutation of the other
'''

def is_permutation(string1: str, string2: str) -> bool:
    if len(string1) <= 1 and len(string2) <= 1:
        return True
    
    characterFrequencyMap = {}
    # map first string with counts
    for char in string1:
        if characterFrequencyMap.get(char):
            characterFrequencyMap[char] += 1
        else:
            characterFrequencyMap[char] = 1

    # decrement counts with second string
    for char in string2:
        if characterFrequencyMap.get(char):
            characterFrequencyMap[char] -= 1
        else:
            return False

    # if all counts are zero, strings are permutations of each other, else false
    for value in characterFrequencyMap.values():
        if value != 0:
            return False
    return True

def run_tests():
    assert is_permutation("", "")
    assert is_permutation("a", "a")
    assert is_permutation("kevin", "nivek")
    assert is_permutation("1234567", "7153642")
    assert is_permutation("tacocat", "tacocat")
    assert not is_permutation("kevin", "niveka")
    assert not is_permutation("Kevin", "nivek")

def main():
    run_tests()

if __name__ == '__main__':
    main()

from parser import *

def testNull():
    input = ",,,"
    output = parseLine(input)
    print("Output after parsing is {} is {}".format(input, output))
    #assert(output == [None])

def testString():
    input = "\"a\"\"b,\",\"abc\",123,456,\"\""
    output = parseLine(input)
    print("Output after parsing {} is {}".format(input, output))

def testEmptyString():
    input = "\"\""
    output = parseLine(input)
    print("Output after parsing {} is {}".format(input, output))

# Test one of each input: filled string, empty string, integer, NULL
def testMixed():
    input = "\"heyo\",\"\",420,,"
    output = parseLine(input)
    print("Output after parsing {} is {}".format(input, output))


def main():
    testString()
    testNull()
    testEmptyString()
    testMixed()

if __name__ == "__main__":
    main()
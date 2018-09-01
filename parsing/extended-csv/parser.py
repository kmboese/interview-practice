
'''
Given a line of csv input, parse the following inputs:
1. String:
    a. Always opened with a double quote and closed with a double quote
    b. Escaped double quotes are allowed as a sequence of two double quotes, 
    i.e. '""'
    c. Strings may contain commas that should not be treated as a delimiter
2. Integer:
    a. Integer fields contain only digits 0-9, with no other characters
3. NULL
    a. NULL fields are fields with nothing in them (comma followed by nothing before the next comma)

You can assume that the input is correct, with all strings correctly quoted, all commas in correct places, etc.

EXAMPLES:
1. 
'''

def parseLine(line):
    tokens = []
    string = ""
    numStr = ""
    i = 0
    while i < len(line):
        string = ""
        numStr = ""
        # Check for a string
        if line[i] == "\"":
            string, i = parseString(line, i)
            tokens.append(string)
        # If not a string, check for integer
        elif isInt(line[i]):
            numStr, i = parseInt(line, i)
            tokens.append(int(numStr))
        # NULL type
        else:
            tokens.append(None)
            
        # Skip the comma
        i += 1

    return tokens

# Parse a line until we see a closing quote
# Ex: "a""b," --> "a"b,"
def parseString(line, i):
    # Skip the opening quote
    i += 1
    string = ""
    while i < len(line):
        if i+1 < len(line) and line[i] == "\"" and line[i+1] != "\"":
            # Skip the closing quote
            i += 1
            break
        # If an escaped double quote is seen, append one double quote and skip the next one 
        elif i+1 < len(line) and line[i] == "\"" and line[i+1] == "\"":
            string += "\""
            i += 2
        # Otherwise, append a character
        else:
            # Skip the closing quote
            if line[i] == "\"":
                i += 1
                break

            string += line[i]
            i += 1

    return string, i

# Check if a character is an int
def isInt(char):
    return char >= '0' and char <= '9'

# Parse an int
def parseInt(line, i):
    numStr = ""
    while i < len(line):
        if not isInt(line[i]):
            return numStr, i
        else:
            numStr += line[i]
            i += 1

    return numStr, i


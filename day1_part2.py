# Open the file called "input.txt" in the same directory as this file.
input_file = open("input.txt", 'r')
# Read the file into a list where every element is a line from the file in order.
# The lines are stored as strings.
input = input_file.readlines()
# Close the file before we start solving.
input_file.close()


def identify_digit(line:str, i:int):
    if line[i].isdigit(): return int(line[i])
    elif line[i:i+3] == "one": return 1
    elif line[i:i+3] == "two": return 2
    elif line[i:i+5] == "three": return 3
    elif line[i:i+4] == "four": return 4
    elif line[i:i+4] == "five": return 5
    elif line[i:i+3] == "six": return 6
    elif line[i:i+5] == "seven": return 7
    elif line[i:i+5] == "eight": return 8
    elif line[i:i+4] == "nine": return 9

    return None


sum = 0
for line in input:
    
    digits = []
    for i in range(len(line)):
        c = identify_digit(line, i)
        if c:
            digits.append(c)
    
    num = int(str(digits[0]) + str(digits[-1]))
    sum += num

print(sum)

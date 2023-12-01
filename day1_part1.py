# Open the file called "input.txt" in the same directory as this file.
input_file = open("input.txt", 'r')
# Read the file into a list where every element is a line from the file in order.
# The lines are stored as strings.
input = input_file.readlines()
# Close the file before we start solving.
input_file.close()


sum = 0
for line in input:
    
    digits = []
    for c in line:
        if c.isdigit():
            digits.append(c)
    
    num = int(digits[0] + digits[-1])
    sum += num

print(sum)

#!/usr/bin/python3

import re

def get_numbers_from_file(filename):
    '''Reads a file and returns a list of numbers
       The list is created by taking the first and last number
       found in each line. If no numbers are found, the line is
       skipped. If there is only one it is used as the first and last
    '''
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    regex = r'[^0-9]' # Regex to remove all non-numbers
    numbers_list = []
    for line in lines:
        just_numbers = re.sub(regex, r'', line)
        if len(just_numbers) == 0:
            # No numbers found in line
            continue
        else:
            # get the first and last number. Could be the same character!!!
            numbers_list.append(int(just_numbers[0]+just_numbers[-1]))
    return numbers_list

# run for example file to check if it is correct
numbers = get_numbers_from_file("example.txt")
print(numbers)
sum_of_numbers = sum(numbers)
print(sum(numbers))

# Check if example is correct
if sum_of_numbers == 142:
    print("Example is Correct. Running on input file")
    numbers = get_numbers_from_file("input.txt")
    print(numbers)
    sum_of_numbers = sum(numbers)
    print(sum_of_numbers)
else:
    print("Example is not correct. Check your code")

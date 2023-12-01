#!/usr/bin/python3

import re

def convert_word_to_number(word):
    # Convert words to numbers
    word = word.replace("one", "1")
    word = word.replace("two", "2")
    word = word.replace("three", "3")
    word = word.replace("four", "4")
    word = word.replace("five", "5")
    word = word.replace("six", "6")
    word = word.replace("seven", "7")
    word = word.replace("eight", "8")
    word = word.replace("nine", "9")
    return word


def get_numbers_from_file(filename, wordToNumber=False):
    '''Reads a file and returns a list of numbers
       The list is created by taking the first and last number
       found in each line. If no numbers are found, the line is
       skipped. If there is only one it is used as the first and last
    '''
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    numbers_list = []
    for line in lines:
        line = line.strip()

        if wordToNumber:
            firstCharIsLetter_regex = r'^[a-z]+'
            while re.search(firstCharIsLetter_regex, line) is not None:
                regex = r'^(one|two|three|four|five|six|seven|eight|nine)?(.*)'
                result = re.search(regex, line)
                if result is not None and result.group(1) is not None:
                    line = convert_word_to_number(result.group(1)) + result.group(2)
                else:
                    line = line[1:]

            lastCharIsLetter_regex = r'[a-z]+$'
            while re.search(lastCharIsLetter_regex, line) is not None:
                regex = r'^(.*?)(one|two|three|four|five|six|seven|eight|nine)$'
                result = re.search(regex, line)
                if result is not None and result.group(2) is not None:
                    line = result.group(1) + convert_word_to_number(result.group(2))
                else:
                    line = line[:-1]

        removeLetters_regex = r'[^0-9]' # Regex to remove all non-numbers
        just_numbers = re.sub(removeLetters_regex, r'', line)

        if len(just_numbers) == 0:
            # No numbers found in line
            continue
        else:
            # get the first and last number. Could be the same character!!!
            numbers_list.append(int(just_numbers[0]+just_numbers[-1]))

    return numbers_list

print("Advent of Code: Day 1 - Part 1 --------------------------------------")
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
    exit()

print()
print("Advent of Code: Day 1 - Part 2 --------------------------------------")
# run for example2 file to check if it is correct
# with word to numbers enabled
numbers = get_numbers_from_file("example2.txt", True)
print(numbers)
sum_of_numbers = sum(numbers)
print(sum(numbers))

# Check if example is correct
if sum_of_numbers == 281:
    print("Example is Correct. Running on input file")
    numbers = get_numbers_from_file("input.txt", True)
    print(numbers)
    sum_of_numbers = sum(numbers)
    print(sum_of_numbers)
else:
    print("Example is not correct. Check your code")
    exit()
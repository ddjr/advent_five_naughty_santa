import time
from sys import argv
script, filename = argv

def advent_of_code_intro(project_num):
    print ""
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  ---------------------------- Welcome to ----------------------------------'
    time.sleep(.1)
    print '  -------------------------- Advent of Code --------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  ------------------ Created by: David Daly 2016 VA ------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  ------- This project was done as part the adventofcode.com coding --------'
    time.sleep(.1)
    print '  ------- challenges. This is project %s. Each project has two parts. -------' % project_num
    time.sleep(.1)
    print '  ------- This program completes both parts. -------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  -------- You can find me on Github at github.com/ddjr --------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    print ""
    time.sleep(.8)
def check_double_letters(letter1, letter2):
    if letter1 == letter2:
        return True
    else:
        return False
def check_vowel(letter):
    vowels = ["a","e","i","o","u"]
    for vowel in vowels:
        if letter == vowel:
            return 1
    return 0
def check_special_strings(letter1, letter2):
    letters = letter1 + letter2
    special_strings = ["ab","cd","pq","xy"]
    for special_string in special_strings:
        if special_string == letters:
            return True
    return False
def open_file(filename):
    txt = open(filename)
    print "Openning file named: %r " % filename
    return txt.read()
def parse_items(_list):
    return _list.split('\n')
def string_to_chars(string):
    chars = list(string)
    return chars
def print_substring(index,name):
    dots_before = index * "."
    substring = name[index] + name[index+1]
    dots_after = ((len(name) - 1) - (index + 1)) * "."
    string = dots_before + substring + dots_after
    print string
def check_nice_year_one(name):
    nice = [False, 0, False]
    for index in range (0, len(name)):
        #if index != len(name)-1:
        #    print_substring(index,name)
        if nice[0] == False and index != len(name)-1:
            nice[0] = check_double_letters(name[index], name[index+1])
        if nice[1] < 3:
            nice[1] += check_vowel(name[index])
        if nice[2] == False and index != len(name)-1:
            nice[2] = check_special_strings(name[index], name[index+1])
    return is_nice_year_one(nice)
def is_nice_year_one(nice):
    if nice[0] == True and nice[1] >= 3 and nice[2] == False:
        return True
    else:
        return False
def check_nice_year_two(name):
    substrings = []
    nice = [False, False]
    for index in range(0, len(name)-1):
        substring = name[index] + name[index+1]
        substrings.append(substring[:])
        if nice[1] == False and index != len(name)-2:
            nice[1] = check_sandwich(name[index],name[index+2])
    nice[0] = check_substring_pairs(substrings)
    return is_nice_year_two(nice)
def is_nice_year_two(nice):
    if nice == [True, True]:
        return True
    else:
        return False
def check_sandwich(letter1,letter2):
    if letter1 == letter2:
        return True
    else:
        return False
def check_substring_pairs(substrings):
    for index1 in range(0, len(substrings)):
        for index2 in range(index1+1, len(substrings)):
            if substrings[index1] == substrings[index2] and index1 + 1 != index2:
                return True
    return False

def interate_through_santas_list(santas_list):
    naughty = [0,0]
    nice = [0,0]
    for name in santas_list:
        name = string_to_chars(name)
        if check_nice_year_one(name):
            nice[0] += 1
        else:
            naughty[0] += 1
        if check_nice_year_two(name):
            nice[1] += 1
        else:
            naughty[1] += 1
    print "there were %s nice kids and %s naughty kids in year 1" % (nice[0], naughty[0])
    print "there were %s nice kids and %s naughty kids in year 2" % (nice[1], naughty[1])

advent_of_code_intro(5)
santas_list = open_file(filename)
santas_list = parse_items(santas_list)
interate_through_santas_list(santas_list)

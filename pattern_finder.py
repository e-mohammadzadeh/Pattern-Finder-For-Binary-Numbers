######################################################################
#############         Erfan Mohammadzadeh            #################
#############      Pattern Finder in Binary Num      #################
######################################################################

import re


def get_binary_string():
	binary_string = input("Enter a binary number (contain only 1s and 0s) to find pattern in it : ")
	flag = True
	while flag:
		for index in binary_string:
			flag = False
			if index != "1" and index != "0":
				binary_string = input("Must be a binary number, Enter again : ")
				flag = True
				break
	return binary_string


def find_pattern_in_binary_string(binary_string):
	pattern = system_forecast(binary_string)
	if not checker(binary_string, pattern):
		print("{} 's pattern is equal to {}.".format(binary_string, pattern))
	else:
		print("Number {} has NOT any pattern!!!".format(binary_string))


def number_separator(binary_string):
	new_string = ""
	for index in binary_string:
		new_string += index + " "
	return new_string


def system_forecast(binary_string):
	regex = re.compile(r'(.+ .+)( \1)+')
	try:
		match = regex.search(number_separator(binary_string)).group(1)
	except AttributeError:
		print("Number {} has NOT any pattern!!!".format(binary_string))
		exit()
	return concatenation(match)


def concatenation(string):
	return string.replace(" ", "")


def checker(string, sub_string):
	return string.replace(sub_string, "")


if __name__ == "__main__":
	find_pattern_in_binary_string(get_binary_string())

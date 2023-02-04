# Assignment 2
# Write a Python program that accepts a hyphen-separated sequence of words 
# as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow

def alphaSort(string):
    '''Returns the words in a hyphen-separated sequence after sorting them alphabetically'''
    return '-'.join(sorted(string.split("-")))

# string = input('Enter your string here... ')
# print(alphaSort(string))
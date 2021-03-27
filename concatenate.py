import sys
from typing import Iterable

def concatenate_list(iterableObject: Iterable) -> str:
    # This method takes in an iterable object, goes over each element, joins them with a comma and returns a string.
    concatenated_str = ','.join(map(str, iterableObject))
    return concatenated_str

def get_input(filename: str) -> Iterable:
    # This method asks the user for a filename, tries to open it, reads the data line by line and returns it inside an iterable.
    try: 
        retrieved_data = open(filename, 'r').read().split()
        return retrieved_data
    except FileNotFoundError: 
        print('Filename not found. Please try again.')
        sys.exit()
    
if __name__ == "__main__":
    print('Enter the filename where the data is stored: ')
    new_string = concatenate_list(get_input(input()))
    print(new_string)
    
def concatenate_list(list: dict):
    # This method takes in a list or dictionary, iterates over it and joins each item with a comma.
    modified_list = ','.join(list)
    return modified_list
    
if __name__ == "__main__":
    letters = ['a','b','c','d','e','f']
    new_string = concatenate_list(letters)
    print(new_string)
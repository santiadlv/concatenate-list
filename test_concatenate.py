from concatenate import concatenate_list, get_input

def test_concatenate_from_list() -> str:
    test_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert concatenate_list(test_list) == '10,9,8,7,6,5,4,3,2,1,0'
    return 'successful'

def test_concatenate_from_file() -> str:
    test_data = get_input('test_data.txt')
    assert concatenate_list(test_data) == 'oh,no,it,sa,tr,ai,nw,re,ck'
    return 'successful'

if __name__ == '__main__':
    print(f'Test from list is: {test_concatenate_from_list()}')
    print(f'Test from file is: {test_concatenate_from_file()}')
    
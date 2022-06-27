def test_get_unique_code(function):
    '''
    The function checks the creation of a unique code for the client
    '''
    print('Function get_unique_code testing:')
    unique_code1='12345'

    if function(unique_code1)==function(unique_code1):
        print('#Test1: fail')
    else:
        print('#Test1: ok')
def to_upper_case(string):
    print('2.', id(string))
    string = 'Cos tAM'
    print('3.', id(string))

if __name__ == '__main__':
    s = 'Hello World'
    print('1.', id(s))
    to_upper_case(s)
    print('4.', id(s))

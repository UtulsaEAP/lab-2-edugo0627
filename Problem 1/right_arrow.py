'''
Lab 2 problem 1: right arrow
Name: Emma J. Verdugo
lab: @2pm
'''

def right_arrow():
    base_char = input('Enter character for base of arrow: ')
    head_char = input('Enter character fo head of arrow: ')

    row1 = '      ' + head_char
    ''' Type your code here. '''
    
    row2 = base_char + base_char + base_char + base_char + base_char + base_char + head_char + head_char
    row3 = base_char + base_char + base_char + base_char + base_char + base_char + head_char + head_char + head_char
    
    print(row1)
    print(row2)
    print(row3)
    print(row2)
    print(row1)

if __name__ == "__main__":
    right_arrow()
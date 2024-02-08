'''
Lab 2 assignment problem 1: right arrow
Name: Emma J. Verdugo
Lab Time: @2pm

'''

def right_arrow():
    base_char = input("Enter firt character: ")
    head_char = input("Enter second character: ")

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
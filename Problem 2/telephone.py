'''
Lab 2 problem 2: Outputing 10 digit phone numbe in the format (xxx) xxx-xxxx
Name: Emma J. Verdugo
Lab: @2pm
'''
def telephone():
    phone_number = int(input())
    ''' Type your code here. '''
    
    last_four = phone_number % 10000
    number2 = phone_number // 10000
    
    middle_three = number2 % 1000
    
    first_three = phone_number // 10000000
    
    print( '(' + str(first_three)+ ')' + ' ' + str(middle_three)+ '-' + str(last_four))


if __name__ == "__main__":
    telephone()
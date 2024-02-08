def telephone():
    phone_number = int(input())
    ''' Type your code here. '''
    
    last_four = phone_number % 10000
    number2 = phone_number // 10000
    
    middle_three = number2 % 1000
    
    first_three = phone_number // 10000000
    
    print(first_three,middle_three,last_four)
    

if __name__ == "__main__":
    telephone()
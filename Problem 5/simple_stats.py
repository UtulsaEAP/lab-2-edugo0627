'''
Lab 2 problem 5: given 4 numbers and finding there avergage and product as floats and intergers 
Name: Emma J. Verdugo
lab: @2pm
'''
def simple_stats():
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    ''' Type your code here. '''
    
    product = num1 * num2 * num3 * num4
    avg = (num1 + num2 + num3 + num4) / 4 
    
    print(f'{product:.0f}',f'{avg:.0f}')
    print(f'{product:.3f}',f'{avg:.3f}')
    
    
if __name__ == "__main__":
    simple_stats()
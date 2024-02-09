'''
Lab 2 problem 3: 
Name: Emma J. Verdugo
lab: @2pm
'''
def caffeine():
    caffeine_mg = float(input())
    ''' Type your code here. '''
    
    hours_6 = float(caffeine_mg)*.5
    hours_12 = float(caffeine_mg)*.5**(12/6)
    hours_24 = float(caffeine_mg)*.5**(24/6)
    
    print(f'After 6 hours: {hours_6:.2f} mg')
    print(f'After 12 hours: {hours_12:.2f} mg')
    print(f'After 24 hours: {hours_24:.2f} mg')
    
if __name__ == "__main__":
    caffeine()
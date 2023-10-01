 
def count_chars():
    lt_5 = "your input is less than 5 characters long."
    gt_5 = "your input is greater than 5 characters long."
    eq_5 = "your input is 5 characters long."
    
    value = input('Enter a string value: ')
    lv = len(value)
    
    if lv < 5:
        print(lt_5)
    elif lv > 5:
        print(gt_5)
    else:
        print(eq_5)

def break_out_on_q_or_Q():

    while True:
        value = input('Enter a value (q or Q to quit): ')
        if value.lower() == 'q':
            break
        print(f'Value is: {value}')
    print('Quitting')

def loop_over_find_not_3_multiple():
    for val in range(1, 51):
        if val % 3 == 0:
            # value is a multiple of 3 so skip it
            continue
        print(f'{val} is not a multiple of 3')
        
def validate_integer_catch_gracefully():
    while (i := input('Enter an integer: ')):
        try:
            int_value = int(i)
            print(f'{int_value} is an int.')
        except ValueError:
            print(f'{i} is not an int. Try again.')
            pass

validate_integer_catch_gracefully()

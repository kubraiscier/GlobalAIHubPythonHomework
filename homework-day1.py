
def getValue(type, message):
    while True:
        try:
            return type(input(message))
        except ValueError:
            print('Please enter a value with expected type!!')
            continue

int_val = getValue(int, 'Enter an integer value : ')
str_val = getValue(str, 'Enter a string value : ')
float_val = getValue(float, 'Enter a float value : ')
bool_val = getValue(bool, 'Enter a boolean value : ') 
list_val = getValue(list, 'Enter a list value : ') 

print('\n')

print("\
First Value  : {}\n\
Second Value : {}\n\
Third Value  : {}\n\
Fourth Value : {}\n\
Fifth Value  : {}\n".format(int_val, str_val, float_val, bool_val,list_val))

print("\
First Type  : {}\n\
Second Type : {}\n\
Third Type  : {}\n\
Fourth Type : {}\n\
Fifth Type  : {}".format(type(int_val), type(str_val), type(float_val), type(bool_val), type(list_val)))
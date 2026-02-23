# handling errors

# common error types

# FileNotFoundError
# KeyError
# IndexError
# TypeError

# try, except, else, finally

# try - wraps an action that could produce errors
# except - what to do if there's an error
# else - what to do if no errors
# finally - what to do next with or without error
# raise - used to create a custom error

try:
    file = open('no_file.txt')
    any_dict = {'any':'any'}
    print(any_dict['wrong_key'])
# except: - this is too broad, specify the error
except FileNotFoundError:
    file = open('safeOpen.txt', 'w')
except KeyError as err_msg:
    print(f'No such key {err_msg}')
else:
    print('All is well')
    content = file.read()
    print(content)
finally:
    file.close()
    print('All done here')


# raising custom exceptions
# example
height = float(input('Whats your height'))
weight = float(input('Whats your weight'))

if height > 3:
    raise ValueError('Omo you too tall oo')
elif weight > 500:
    raise ValueError('Is that even possible?')

bmi = weight / height ** 2

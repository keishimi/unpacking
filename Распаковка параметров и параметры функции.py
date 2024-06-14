
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
values_list=[False, 52, 'run']
values_dict={'b':69, 'c':'cloud', 'a':True}

values_list_2=[83, False]

print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2,42)

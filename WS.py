#1
def de_none(lst):
    return [value for value in lst if value is not None]


values = [1, None, "hello", None, 5.6]
new_values = de_none(values)
print(new_values)

#2
def list_insert(ref_list, start, num, rep):
    for i in range(rep):
        ref_list.insert(start, num)
    return ref_list
my_list = [1, 2, 3, 4, 5]
position = 2
number = 9
repetitions = 3
result = list_insert(my_list, position, number, repetitions)
print("Результат:", result)

#3
def get_elem(d, k):
    return d.get(k, None)

my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
key = 'key2'
result = get_elem(my_dict, key)
print("Результат:", result)

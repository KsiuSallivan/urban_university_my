calls = 0

def count_calls():
    global calls
    calls = calls + 1
    return calls


def string_info(string):
    count_calls()
    string_play = (len(string), string.upper(), string.lower())
    return string_play


def is_contains(string, list_to_search):
    count_calls()
    list_to_search_new = []
    for i in list_to_search:
        list_to_search_new.append(i.lower())
    if string.lower() in list_to_search_new:
        find_string = True
    else:
        find_string = False
    return find_string


print(string_info('В кофемашине на работе закончилось молоко'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(string_info('В кофемашине на работе закончилось молоко'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)
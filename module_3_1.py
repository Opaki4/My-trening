calls = 0

def count_calls(call):
    global calls
    calls += call
    return calls
def string_info(string):
    a = [len(string), string.upper(), string.lower()]
    count_calls(1)
    return tuple(a)
def is_contains(string, list_to_search):
    b = []
    count_calls(1)
    for i in list_to_search: #
        b.append(i.lower()) #
    return string.lower() in b
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
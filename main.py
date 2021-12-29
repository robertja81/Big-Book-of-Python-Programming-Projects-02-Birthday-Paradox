## Birthday Analysis

from random import randrange, choice

### Main ###
print('How many birthdays should I generate?')
num_birthdays = input()
print('Here are ' + num_birthdays + ' birthdays')

birthday_dict = {'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}
day_tuples = {'Jan': 31, 'Feb': 28, 'Mar': 30, 'Apr': 30, 'May': 31, 'Jun': 31, 'Jul': 31, 'Aug': 31, 'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31}
birthday_list = []

index = 0

while index < int(num_birthdays):
    #birthday_list.append(randrange(0, 100))
    get_month = choice(birthday_dict['month'])
    get_max_days = day_tuples[get_month]
    get_random_days = randrange(1, get_max_days)
    birthday_list.append(get_month + ' ' + str(get_random_days))
    index += 1
print(birthday_list)

outer_counter = 0
matches = 0
list_of_matches = []
while outer_counter < len(birthday_list):
    inner_counter = 0
    while inner_counter < len(birthday_list):
        if birthday_list[outer_counter] == birthday_list[inner_counter] and outer_counter != inner_counter:
            matches += 1
            list_of_matches.append(birthday_list[outer_counter])
        inner_counter += 1
    outer_counter += 1

if matches > 0:
    print('We have ' + str(len(list_of_matches)) + ' matching birthdays!')
    for birthday in list_of_matches:
        print(birthday)
        print('\n')
else:
    print('There were no matching birthdays found!')
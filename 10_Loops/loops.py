count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4


count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break


count = 0
while count < 5:
    if count == 3:
        continue
    print(count)
    count = count + 1

    person = {
        'first_name': 'Asabeneh',
        'last_name': 'Yetayeh',
        'age': 250,
        'country': 'Finland',
        'is_marred': True,
        'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address': {
            'street': 'Space street',
            'zipcode': '02210'
        }
    }
    for key in person:
        print(key)

    for key, value in person.items():
        print(key, value)  # this way we get both keys and values printed out

#n python when statement is required (after semicolon), but we don't like to execute any code there, we can write the word pass to avoid errors. Also we can use it as a placeholder, for future statements.

for number in range(6):
    pass

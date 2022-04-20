persons = []
dataarr = []


def get_data(var_name,text):
    data = input(text)
    while data == '':
        data = input('please write information: ')
    dataarr.append([var_name,data])


def save_to_file(person):
    file = open('address_book.txt','a')
    for data in person:
        file.write(f'{data} = {person[data]}\n')
    file.write('---------------------------- :\n')

def create_person(dataarr):
    person = {}
    for x in dataarr:
        person [x[0]] = x[1]
    save_to_file(person)


get_data('name','Enter your name: ')
get_data('age','Enter your age: ')
get_data('address','Enter your address: ')
get_data('tel','Enter your number: ')
get_data('work','Enter your job: ')

create_person(dataarr)



LOGIN_DATA = {
    'valid_email': 'test2025@yahoo.com',
    'valid_password': 'Qa1234!',
    'invalid_email': 'wrong@test.com',
    'invalid_password': 'wrongpass'
}

URLS = {
    'login_page': 'http://34.141.58.52:8080/#/login',
    'main_page': 'http://34.141.58.52:8080/#/',
    'profile_page': 'http://34.141.58.52:8080/#/profile',
    'pet_new_page': 'http://34.141.58.52:8080/#/pet_new',
    'pet_edit_page': 'http://34.141.58.52:8080/#/pet-edit'
}

PET_TYPES ={
    'cat': 'cat',
    'dog': 'dog',
    'hamster': 'hamster',
    'reptile' : 'reptile',
    'parrot' : 'parrot'
}
PET_DATA = {
    'pet1': {
        'name': 'Карамелька',
        'type': PET_TYPES['cat'],
        'age': '1'
    },
    'pet2': {
        'name': 'Коржик',
        'type': PET_TYPES['cat'],
        'age': '2'
    },
    'pet3': {
        'name': 'Компот',
        'type': PET_TYPES['cat'],
        'age': '3'
    },
    'pet3_edited': {
        'name': 'Компот',
        'type': PET_TYPES['hamster'],
        'age': '3'
    },
    'pet4': {
        'name': 'Космос',
        'type': PET_TYPES['dog'],
        'age': '4'
    }

}

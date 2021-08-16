import json
import re
from tinydb import TinyDB


db = TinyDB('test.json')


def check_form(form):
    '''
    Проверяем форму
    '''
    data = {}
    keys_lst = form.keys()
    for key in keys_lst:
        data[key] = check_param(form[key])
    forms = db.all()
    for i in forms:
        form_keys_list = list(i.keys())
        form_keys_list.remove('name')
        if len(form_keys_list) > 0 and set(form_keys_list).issubset(keys_lst) and all([data[key]['type'] == i[key] for key in form_keys_list]):
            return f"Найдено совпадение {i['name']}: {form_keys_list} в {keys_lst}"
    return json.dumps(form)


def check_param(value) -> dict:
    '''
    Проверяем различные параметры
    '''
    if check_date(value):
        value_type = "date"
    elif check_phone(value):
        value_type = "phone"
    elif check_email(value):
        value_type = "email"
    else:
        value_type = "text"
    return {"value": value, "type": value_type}


def check_email(email):
    '''
    проверяем адрес почты через регулярку.
    '''
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return email if(re.match(regex, email)) else False


def check_phone(phone):
    '''
    проверяем телефон. Сначала получаем список из цифр, проверяем и затем пересоздаем его.
    вообще я бы смотрел на страну по коду, затем отрезал бы код страны и оставлял номер цифрами. Удобнее для сервисов.
    '''
    phone = ''.join(re.findall(r'\d+', phone))
    return phone if len(phone) == 11 and phone.startswith('7') else False


def check_date(date):
    '''
    проверяем дату. Вообще в идеале привести бы к общему виду здесь, как с телефоном,
    чтобы не плодить далее проверку еще раз.
    '''
    regex1 = "^\s*(3[01]|[12][0-9]|0?[1-9])\.(1[012]|0?[1-9])\.((?:19|20)\d{2})\s*$"  # DD.MM.YYYY
    regex2 = "^\s*((?:19|20)\d{2})\.(1[012]|0?[1-9])\.(3[01]|[12][0-9]|0?[1-9])\s*$"  # YYYY.MM.DD
    return date if any((re.match(regex1, date), re.match(regex2, date))) else False


# TODO: может добавить проверку на число? pk юзера, к примеру.
# def check_number(number):
#     pass


def create_form(json_data):
    '''
    Функция создания шаблона для формы
    '''
    if 'name' in json_data:
        db.insert(json_data)
        response = f"Создана форма {json_data['name']}"
    else:
        response = "В форме отсутствуем имя (name)"
    return response


# parseTest
Тестовое задание по парсингу. Устанавливаем:

``` json
pip install -r requirements.txt
```

Поднимается с помощью Flask, БД - tinyDB. Чтобы добавить форму, можно отправлять на страницу */create_form* custom вида:

``` json
{
  "name": "Register form",
  "user_email": "email", 
  "date_join": "date", 
  "phone": "phone", 
  "login": "text"
}

```

На странице */get_form* отправляем данные, после чего получаем название формы (и список сравниваемых полей).

Сравнение идет по названию и типу поля.

Текущая база данных - test.json.

from flask import Blueprint, render_template
lab2=Blueprint('lab2', __name__)


@lab2.route("/lab2/example")
def example():
    name, group, num, n= 'Яцынина Юлия', 'ФБИ-14', 3, 2
  
    fruits=[
        {'name':'Лимон', 'price': 70},
        {'name':'Яблоко', 'price': 150}, 
        {'name':'Апельсин', 'price': 120}, 
        {'name':'Дыня', 'price': 300},
        {'name':'Арбуз', 'price': 350}
    ]

    books = [
        {'aut': 'Джоан Роулинг', 'naz': 'Гарри Поттер и узник Азкабана', 'ganr': 'Фэнтези', 'str': '544'},
        {'aut': 'Наталья Щерба', 'naz': 'Часодеи', 'ganr': 'Фантастика', 'str': '400'},
        {'aut': 'Маркус Зусак', 'naz': 'Книжный вор', 'ganr': 'Проза', 'str': '448'},
        {'aut': 'Стивен Кинг', 'naz': 'Зелёная миля', 'ganr': 'Ужасы', 'str': '384'},
        {'aut': 'Михаил Булгаков', 'naz': 'Мастер и Маргарита', 'ganr': 'Классика', 'str': '480'},
        {'aut': 'Анджей Сапковский', 'naz': 'Ведьмак:Меч предназначения', 'ganr': 'Фэнтези', 'str': '384'},
        {'aut': 'Джек Лондон', 'naz': 'Белый клык', 'ganr': 'Классика', 'str': '224'},
        {'aut': 'О.Генри', 'naz': 'Дары волхвов', 'ganr': 'Классика', 'str': '384'},
        {'aut': 'Джейн Остин', 'naz': 'Гордость и предубеждение', 'ganr': 'Классика', 'str': '384'},
        {'aut': 'Туве Янссон', 'naz': 'Всё о муми-троллях', 'ganr': 'Сказки', 'str': '880'}
        ]

    return render_template('example.html',
                           name=name, group=group, num=num, n=n,
                           fruits=fruits, books=books)


@lab2.route("/lab2/")
def labb2():
    return render_template('lab2.html')


@lab2.route("/lab2/sweets")
def sw():
    return render_template('sweets.html')
from flask import Flask, redirect, url_for, render_template
app=Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return '''
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, WEB-программирование, Лабораторные работы</title>
        <link rel="stylesheet" href="''' +url_for('static', filename='lab1.css')+ '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>
        <h2>Меню</h2>
        <ol>
            <li><h3><a href="/lab1">Лабораторная работа 1</a></h3></li>
        </ol>
        <footer>
            &copy; Юлия Яцынина, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@app.route("/lab2/example")
def example():
    return render_template('example.html')

@app.route("/lab1")
def lab1():
    return '''
<!doctype html>
<html>
    <head>
        <title>Яцынина Юлия Сергеевна, лабораторная 1</title>
        <link rel="stylesheet" href="''' +url_for('static', filename='lab1.css')+ '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>Web-сервер на flask</h1>

        <p>Flask — фреймворк для создания веб-приложений на языке 
            программирования Python, использующий набор инструментов
            Werzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </p>

        <h2><a href="/menu" target="_blank">Меню</a></h2>

        <h2>Реализованные роуты</h2>
        <ul>
            <li><a href="/lab1/dub" target="_blank">/lab1/dub - Дуб</a></li>
            <li><a href="/lab1/student" target="_blank">/lab1/student - Студент</a></li>
            <li><a href="/lab1/python" target="_blank">/lab1/python - Python</a></li>
            <li><a href="/lab1/golub" target="_blank">/lab1/golub - Голубь</a></li>
        </ul>

        <footer>
            &copy; Юлия Яцынина, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@app.route('/lab1/dub')
def dub():
    return '''
<!doctype html>
<html>
    <head>
        <title>Яцынина Юлия Сергеевна, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <link rel="stylesheet" href="''' +url_for('static', filename='lab1.css')+ '''">
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='dub.jpg')+'''">
        <footer>
            &copy; Юлия Яцынина, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@app.route('/lab1/student')
def stud():
    return '''
<!doctype html>
<html>
    <head>
        <title>Яцынина Юлия Сергеевна, лабораторная 1</title>
        <link rel="stylesheet" href="''' +url_for('static', filename='lab1.css')+ '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        <h1>Яцынина Юлия Сергеевна</h1>
        <img src="''' + url_for('static', filename='logo.png')+'''">
        <footer>
            &copy; Юлия Яцынина, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@app.route('/lab1/python')
def python():
    return '''
<!doctype html>
<html>
    <head>
        <title>Яцынина Юлия Сергеевна, лабораторная 1</title>
        <link rel="stylesheet" href="''' +url_for('static', filename='lab1.css')+ '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        <h1>Python</h1>
        <img src="''' + url_for('static', filename='python.png')+'''" class="python">
        <p>
            Python — высокоуровневый язык программирования общего назначения с динамической строгой
            типизацией и автоматическим управлением памятью, ориентированный на повышение производительности
            разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на
            нём программ.
        </p>
        <p>
            Разработка языка Python началась в конце восьмидесятых годов двадцатого столетия. Для распределенной
            операционной системы «Amoeba» понадобился расширяемый скриптовый язык, и сотрудник голландского
            института Гвидо ван Россум начал писать такой язык в свободное время. Уже в тысяча девятьсот
            девяносто первом году Гвидо опубликовал первый код. Название языка, несмотря на созвучность с
            названием семейства неядовитых змей, произошло от другого. Разработчик назвал язык в честь известного
            британского юмористического телевизионного шоу семидесятых — «Летающий цирк Монти Пайтона».
            Среди пользователей Python часто называют просто «Питон».
        </p>
        <p>
            У Python сильные позиции в серверной разработке, AI, Big Data, в программировании в сфере обучения
            и науки. В веб-разработке Python востребован в бэкенд части-разработке. Фронтенд скорее всего не
            для Python, так как в этой нише царствует JavaScript.
        </p>

        
        <footer>
            &copy; Юлия Яцынина, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@app.route('/lab1/golub')
def golub():
    return '''
<!doctype html>
<html>
    <head>
        <title>Яцынина Юлия Сергеевна, лабораторная 1</title>
        <link rel="stylesheet" href="''' +url_for('static', filename='lab1.css')+ '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        <h1>Голубь</h1>
        <img src="''' + url_for('static', filename='gol.jpg')+'''" class="gol">
        <p>
            Голуби многим людям кажутся скучными и банальными птицами, которых можно встретить на каждом шагу
            в любом городе. Но это далеко не так! Например, существуют не только городские, но и дикие голуби,
            обитающие в лесах.
        <p>
            Эти птица способна прожить до 20 лет, а то и больше, особенно если обеспечить ей достойный уход.
            Глаза у голубей примерно втрое более чувствительные, чем у людей. Они воспринимают порядка 75 кадров в секунду.
            Некоторые виды голубей являются деликатесом в ряде стран. Их мясо, кстати, по питательности превосходит куриное в несколько раз.
            Благодаря уникальному строению глаз голуби могут смотреть прямо на Солнце.
            Почти все виды голубей подбирают себе пару раз и на всю жизнь.
            Они только кажутся неуклюжими, когда топчутся по земле. В воздухе же голубь может развивать скорость до 70-75 км/ч.
            Голубь считается птицей мира во множестве стран, и памятники этой птице можно найти в трех десятках городов по всему миру.
            На теле взрослого голубя насчитывается около 10.000 перьев.
        </p>
        
        <footer>
            &copy; Юлия Яцынина, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
'''
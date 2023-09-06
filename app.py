from flask import Flask
app=Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return """
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, WEB-программирование, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>
        <h2>Меню</h2>
        <h3><a href="/lab1">Лабораторная работа 1</a></h3>

        <footer>
            &copy; Юлия Яцынина, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
"""

@app.route("/lab1")
def lab1():
    return """
<!doctype html>
<html>
    <head>
        <title>Яцынина Юлия Сергеевна, лабораторная 1</title>
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

        <footer>
            &copy; Юлия Яцынина, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
"""
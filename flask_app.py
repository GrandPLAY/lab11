from flask import Flask
import math

app = Flask(__name__)

@app.route('/')
def start():
    return 'Доступные операции:<br> 1. Сложение: /add/a/b<br> 2. Вычитание: /sub/a/b<br> 3. Умножение: /mul/a/b<br> 4. Деление: /div/a/b<br> 5. Степень: /pow/a/b<br> 6.  Кв. корень: /sqrt/a<br> 7. Синус: /sin/a<br> 8. Косинус: /cos/a<br> 9. Тангенс: /tan/a'

@app.route('/add/<a>/<b>')
def add(a, b):
    return str(float(a) + float(b))

@app.route('/sub/<a>/<b>')
def sub(a, b):
    return str(float(a) - float(b))

@app.route('/mul/<a>/<b>')
def mul(a, b):
    return str(float(a) * float(b))

@app.route('/div/<a>/<b>')
def div(a, b):
    if b == '0':
        return 'error'
    else:
        return str(float(a) / float(b))

@app.route('/pow/<a>/<b>')
def pow(a, b):
    return str(float(a) ** float(b))

@app.route('/sqrt/<a>')
def sqrt(a):
    if float(a) < 0:
        return 'error'
    else:
        return str(float(a) ** 0.5)

@app.route('/sin/<a>')
def sin(a):
    с = math.sin(float(a))
    return str(с)

@app.route('/cos/<a>')
def cos(a):
    с = math.cos(float(a))
    return str(с)

@app.route('/tan/<a>')
def tan(a):
    if float(a) % (math.pi / 2) == 0:
        return 'error'
    else:
        с = math.tan(float(a))
        return str(с)
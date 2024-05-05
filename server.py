from flask import Flask, render_template, url_for, request
from random import choice


list_color = [
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f'
]
list_password = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '!', '"', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '', '{', '|', '}', '~'
]
app = Flask(__name__)


def random_password(lenght):
    password = ''
    for i in range(lenght):
        password += choice(list_password)
    return password


@app.route('/greeting')
def greeting():
    return render_template('greeting.html', title='Рандомайзеры')


@app.route('/random/color')
def color():
    color = '#'
    for i in range(6):
        color += choice(list_color)
    return render_template('color.html', color=color, title="Рандомайзер цветов")


@app.route('/random/password', methods=['POST', 'GET'])
def password():
    if request.method == 'GET':
        password = random_password(8)
        return render_template('password.html', password=password, value='8', title="Рандомайзер паролей")
    elif request.method == 'POST':
        lenght = request.form['range']
        password = random_password(int(lenght))
        return render_template('password.html', password=password, value=lenght, title="Рандомайзер паролей")


@app.route('/random/number', methods=['POST', 'GET'])
def number():
    if request.method == 'GET':
        number = choice(range(1, 101))
        return render_template('number.html', number=number, value_min=1, value_max=100, title="Рандомайзер числа")
    elif request.method == 'POST':
        number_min = request.form['number_min']
        number_max = request.form['number_max']
        number = choice(range(int(number_min), int(number_max) + 1))
        return render_template('number.html', number=number, value_min=number_min, value_max=number_max, title="Рандомайзер числа")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
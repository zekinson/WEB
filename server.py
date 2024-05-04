from flask import Flask, render_template, url_for
from random import choice


list_color = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']
app = Flask(__name__)

@app.route('/greeting')
def greeting():
    return render_template('greeting.html', title='Рандомайзеры')


@app.route('/random/color')
def color():
    color = '#'
    for i in range(6):
        color += choice(list_color)
    return render_template('color.html', color=color, title="Рандомайзер цветов")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
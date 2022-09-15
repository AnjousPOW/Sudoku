from sydoky_app import app
from flask import render_template, request
from sydoky_app.sydoky.models import grid, victory, gameOver


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


def pri_arr():
    for i in range(9):
        for j in range(9):
            print(grid[i][j])


@app.route('/tablo', methods=['GET', 'POST'])
def Data_input():
    global gameOver

    if request.method == 'POST':
        for i in range(9):
            for j in range(9):
                try:
                    grid[i][j] = int(request.form.get(str(i) + str(j)))
                except:
                    grid[i][j] = 0

    if victory():
        gameOver = True

    return render_template('Tablo.html', grid=grid, gameOver=gameOver)


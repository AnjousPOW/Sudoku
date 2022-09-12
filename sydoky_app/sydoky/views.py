from sydoky_app import app
from flask import render_template, request
from sydoky_app.sydoky.models import grid

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
    if request.method == 'POST':
        for i in range(9):
            for j in range(9):
                try:
                    grid[i][j] = int(request.form.get(str(i) + str(j)))
                except:
                    grid[i][j] = 0

        print(grid)

    return render_template('Tablo.html', grid=grid)



# for i in range(9):
#     for j in range(9):
#         if grid[0][j] == grid[i][j]:
#             print('символы совподают')
#             break
#
# for i in range(9):
#     for j in range(9):
#         if grid[i][0] == grid[i][j]:
#             print('символы совподают')
#             break
#
# for i in range(0, 9, 3):
#     for j in range(0, 9, 3):
#         s = set()
#         for dx in range(3):
#             for dy in range(3):
#                 s.add(grid[i + dx][j + dy])
#
#         if len(s) != 9:
#             print('символы равны')

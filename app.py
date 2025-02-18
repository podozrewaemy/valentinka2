from flask import Flask, render_template

# Создаем приложение Flask
app = Flask(__name__)

# Главная страница
@app.route('/')
def valentine():
    return render_template('valentine.html')

# Запускаем сервер
if __name__ == '__main__':
    app.run(debug=True)
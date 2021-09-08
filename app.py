from flask import Flask, request, render_template

from services import generate_msg


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method == 'POST':
        data = request.get_json(force=True)
        return generate_msg(data)


@app.errorhandler(404)
def error_404(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()

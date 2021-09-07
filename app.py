from flask import Flask, request, render_template

from services import generate_msg


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method == 'POST':
        data = request.get_json(force=True)
        animal, sound, count = data.get('animal'), data.get('sound'), data.get('count')
        return generate_msg(animal, sound, count)


if __name__ == '__main__':
    app.run()

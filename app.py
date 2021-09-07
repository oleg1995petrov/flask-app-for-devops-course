from flask import Flask, request, render_template

from services import get_animal_img, generate_message


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method == 'POST':
        content = request.get_json(force=True)
        animal = content.get('animal')
        sound = content.get('sound')
        count = content.get('count')
        return generate_message(animal, sound, count)


if __name__ == '__main__':
    app.run()

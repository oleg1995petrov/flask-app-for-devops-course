from flask import Flask, request, render_template

from services import generate_msg
from werkzeug.exceptions import BadRequest


RED = '\033[32m'
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            data = request.get_json(force=True)
        except BadRequest:
            return ('Make sure you have passed the right data. '
                    'Here is an example:\n'
                    f"    {RED}curl -X POST -d '"
                    '{"animal": "frog", "sound": "kwa", "count": 5} '
                    'localhost:8080\n')
        return generate_msg(data)
    else:
        return render_template('home.html')


@app.errorhandler(404)
def error_404(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host="0.0.0.0")
from flask import Flask, render_template, request

app = Flask(__name__)

SPORTS = ['basketball', 'soccer', 'frisbee']


@app.route('/')
def index():
    return render_template('index.html', sports=SPORTS)


@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    sport = request.form.get('sport')

    if not name or sport not in SPORTS:
        return render_template('failure.html')
    else:
        return render_template('success.html')

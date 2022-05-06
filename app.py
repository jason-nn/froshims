from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    if not request.form.get('name') or request.form.get('sport') not in ['basketball', 'soccer', 'frisbee']:
        return render_template('failure.html')
    else:
        return render_template('success.html')

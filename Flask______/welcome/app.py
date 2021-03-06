from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def rootpage():
    name = ''
    if request.method == 'POST' and 'username' in request.form:
        name = request.form.get('username')
    return render_template('index.html', name1=name)


app.run(debug=True)
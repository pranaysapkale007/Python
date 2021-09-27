from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = ''
    if request.method == 'POST' and 'weight' in request.form:
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi = calc_bmi(weight, height)
    return render_template("bmi_calc.html", bmi_calculated=bmi)


def calc_bmi(weight, height):
    return round((weight / ((height / 100) ** 2)), 2)


app.run()

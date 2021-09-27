from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def emp_details():
    name = ''
    mobile = ''
    if request.method == 'POST' and 'emp_name' in request.form:
        name = request.form.get('emp_name')
        mobile = request.form.get('emp_mb')
    return render_template("emp_template.html", name=name, mobile=mobile)


app.run()

from flask import Flask, url_for, request
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    title = 'home'
    return render_template('home.html', title=title)


@app.route('/register')
def register():
    title= 'register'

    if request.method == "POST":
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        
    return render_template('register.html', title=title)



if __name__ == '__main__':
    app.run(debug=True)

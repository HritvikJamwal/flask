from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def first():
    return render_template('login.html')

database = {'hritvik': '1234', 'jamwal': '5678'}

@app.route('/form_login', methods=['POST', 'GET'])
def login():
    name1 = request.form['username']
    password1 = request.form['password']
    if name1 not in database:
        return render_template('login.html', info='User not found')
    else:
        if database[name1] != password1:
            return render_template('login.html', info="Invalid Password")
        else:
            return render_template('home.html', name= name1)





if __name__ == '__main__':
    app.run()

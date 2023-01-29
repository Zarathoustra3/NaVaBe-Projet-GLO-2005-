from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/sign-in')
def sign_in():
    return render_template('sign-in.html')
@app.route('/submit')
def submit():
    return "Traitement de Données"
@app.route('/password-recovery')
def password_recovery():
    return render_template('password-recovery.html')

if __name__ == '__main__':
    app.run(debug=True)
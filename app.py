from flask import Flask, render_template, request, url_for, redirect
from static.script.connection_and_registration import  is_client_connectable
app = Flask(__name__)

@app.route('/')
@app.route('/welcome',methods = ['POST'])
def welcome():
    """
     Affiche la page de bienvenue de note site
    :return: welcome.html
    """
    return render_template('welcome.html')

@app.route('/login',methods = ['POST','GET'])
def login(msg:str =""):
    """
    Login du client sur notre site
    :return: sign-in.html
    """
    if not request.form.get('msg') is None:
        msg= request.form.get('msg')
    return render_template('login.html',MsgError=msg)

@app.route('/sign-in')
def sign_in():
    """
    Inscription du client de notre site
    :return: sign-in.html
    """
    return render_template('sign-in.html')

@app.route('/submit',methods = ['POST'])
def submit():
    """
    Vérification des données fournit sur le site lors du login ou/et de l'inscription
    @login : - page demandant soumission : login.html
             - page d'après : main.html
    @signin : - page demandant soumission : sign-in.html
             - page d'après : welcome.html (avec un message)

    @Auteur : Bertrand A

    :return: La page qui demande la soumission si les infos ne sont pas correctes
             la page d'après soumission sinon.

    """
    submit_page = request.form.get('name_page')

    if submit_page == 'login':
        """
        Routine de traitement pour la connexion
        """
        email = request.form.get('email')
        password =request.form.get('password')

        if not is_client_connectable(email, password):
            return redirect(url_for('login',msg="Courriel ou Mot de passe invalide"))

    if submit_page == 'sign-in':
        """
        Routine de traitement pour l'enregistrement 
        """
        pass
    return redirect(url_for('main'))

@app.route('/main')
def main():
    """
    Cette fonction doit permettre à l'utilisateur de naviguer sur NaVaBe, une fois ce dernier connecté.
    La Page html renvoyé est le tableau de bord du site.
    L'utilisateur doit être capable de faire de recherches, voir le profil d'un producteur ou d'un autre user
    Laisser un commentaire sur les autres (et voir exprimer sa satisfaction aussi) etc ...
    Cette fonction peut utiliser d'autres fonctions qui doivent être créé dans le dossier script.

    @Auteur : Bertrand A

    :return: main.html
    """
    return render_template('main.html')

@app.route('/password-recovery')
def password_recovery():
    return render_template('password-recovery.html')

if __name__ == '__main__':
    app.run(debug= True)
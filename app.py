from flask import Flask, render_template, request, url_for, redirect
from static.script import traitement_formulaire
app = Flask(__name__)

@app.route('/')
@app.route('/welcome')
def welcome():
    """
     Affiche la page de bienvenue de note site
    :return: welcome.html
    """
    return render_template('welcome.html')

@app.route('/login',methods = ['GET','POST'])
def login(msg:str =""):
    """
    Login du client sur notre site
    :return: sign-in.html
    """
    if not request.args.get('msg') is None:
        msg= request.args.get('msg')
    return render_template('login.html',MsgError=msg)

@app.route('/sign-in')
def sign_in():
    """
    Inscription du client de notre site
    :return: sign-in.html
    """
    return render_template('sign-in.html')

@app.route('/submit',methods = ['GET','POST'])
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
    id = request.args.get('email')
    password =request.args.get('password')
    print( "id :{} , password : {}".format(id,password))
    if not traitement_formulaire.traitement_login(id,password):
        return redirect(url_for('login',msg="Courriel ou Mot de passe invalide"))
    return redirect(url_for())

@app.route('/main', methods =['POST'])
def main():
    """
    Cette fonction doit permettre à l'utilisateur de naviguer sur NaVaBe, une fois ce dernier connecté
    La Page html renvoyé est le tableau de bord du site.
    L'utilisateur doit être capable de faire de recherches, voir le profil d'un producteur ou d'un autre user
    Laisser un commentaire sur les autres (et voir exprimer sa satisfaction aussi) etc ...
    Cette fonction peut utiliser d'autres fonctions qui doivent être créé dans le dossier script.

    @Auteur : Bertrand A

    :return: main.html
    """

@app.route('/password-recovery')
def password_recovery():
    return render_template('password-recovery.html')

if __name__ == '__main__':
    app.run()
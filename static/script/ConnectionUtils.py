"""
Ce fichier contient l'ensemble des fonctions nécessaires pour l'établissement d'une connection au serveur
Et aussi l'enregistrement dans la BDD.
"""
from flask import flash
import mysql.connector as connector
import smtplib as smtp
from email.message import EmailMessage
import string
import secrets


def insert_to_DB(table: str, values: dict,
                 user='NaVaBe_Project', password='GLO-2005') -> bool:
    """
    Permet d'insérer des valeurs dans la base de données

    :param table: Nom de la table dans la base de données
    :param values: dictionnaire des valeurs à insérer
    :param user: utilisateur (Par défaut NaVaBe_Project)
    :param password: mot de passe de l'utilisateur
    :return: confirmation de l'opération
    """
    completed_operation = False


def generate_pass(length: int = 12, with_letters: bool = True, with_special_chars: bool = True) -> str:
    """
    Génère un mot de passe de facon aleatoire pour confirmer le mail du client ou
    pour récupérer un compte.

    :param with_letters: Active les lettres
    :param with_special_chars: Active les chars spéciaux
    :param length: Longueur de mot de passe à générer
    :return: le mot de passe
    """
    letters = ''
    digits = string.digits  # chiffres
    special_chars = ''

    if with_letters:
        letters = string.ascii_letters

    if with_special_chars:
        special_chars = string.punctuation

    keyboard_complete = letters + digits + special_chars
    pwd_length = length

    password = str()
    for i in range(pwd_length):
        password += ''.join(secrets.choice(keyboard_complete))

    return password


def is_client_connectable(email: str, password: str) -> bool:
    """
    Vérifie si le client est connectable c.-à-d. Les identifiants fournis sont corrects
    et existe dans la base de données
    :param email: mail du client
    :param password:
    :return: True si les identifiants sont corrects, False sinon
    """
    is_client_connectable = False
    try:
        connection = connector.connect(host='localhost',
                                       database='navabe',
                                       user='root',
                                       password='Clervie2014!',
                                       auth_plugin='mysql_native_password')
        cursor = connection.cursor()
        request = "SELECT mot_de_passe FROM clients WHERE email = " + "'" + email + "'"

        cursor.execute(request)
        mot_de_passe = cursor.fetchone()

        if not mot_de_passe is None:
            mot_de_passe = mot_de_passe[0]

            if len(mot_de_passe) > 0:
                if mot_de_passe == password:
                    is_client_connectable = True

    except connector.Error as error:
        flash('Une erreur est survenue ...', 'alert')

    return is_client_connectable


def registration() -> None:
    """
    Pour l'enregistrement dans la BDD de nos entités (Entreprise, Particulier, Produit)
    Une fois l'enregistrement d'une entreprise ou d'un particulier accompli, un mail de confirmation
    doit lui être envoyé pour qu'il active son compte.
    :return:
    """
    pass
def recovery(data: dict) -> bool:
    """

    :param data:
    :return:
    """

def send_email(name: str, mail_receiver: str, message: str = '', subject: str = '') -> None:
    """
    Permet d'envoyer des mails aux clients, par défaut la fonction envoie un mail de bienvenu.
    Les paramètres name et mail sont obligatoires.
    Les paramètres message et subject doivent être passés ensemble.

    :param name: Nom de la personne
    :param mail_receiver: Courriel de la personne
    :param message: Le message
    :param subject: Le sujet du message
    :return: None
    """
    navabe_user_mail = 'pnavabe@gmail.com'
    msg = "Bonjour {} \n\n" \
          "L'équipe du projet NaVaBe vous souhaite la bienvenue dans son réseau.\n" \
          "Dans le but de confirmer votre courriel nous vous demandons de suivre le lien : \n\n{}\n\n\n" \
          "Cordialement, \nLa NaVaBe Team \n".format(name, "https://localhost:5000/confirm")
    sujet = "Bienvenu Chez NaVaBe !"

    if len(message) > 0 & len(subject) > 0:
        msg = message
        sujet = subject

    message_mail = EmailMessage()
    message_mail['from'] = navabe_user_mail
    message_mail['to'] = mail_receiver
    message_mail['subject'] = sujet
    message_mail.set_content(msg)

    server = smtp.SMTP_SSL('smtp.gmail.com', 465)
    server.login(navabe_user_mail, 'sortcwnjprpmlmfz')
    server.sendmail(navabe_user_mail, mail_receiver, message_mail.as_string())


if __name__ == "__main__":
    # print(is_client_connectable('Navabe@root.ca', "Projet-Glo-2005"))
    send_email("Bertrand A", "beawe@ulaval.ca")

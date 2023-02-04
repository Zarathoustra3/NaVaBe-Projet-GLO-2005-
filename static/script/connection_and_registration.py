"""
Ce fichier contient l'ensemble des fonctions nécessaires pour l'établissement d'une connection au serveur
Et aussi l'enregistrement dans la BDD.
"""
import mysql.connector as connector
import smtplib as smtp
from email.message import EmailMessage

def is_client_connectable(email : str, password :str) -> bool:
    """
    Vérifie si le client est connectable c.-à-d. Les identifiants fournis sont corrects
    et existe dans la base de données
    :param email: mail du client
    :param password:
    :return: True si les identifiants sont corrects, False sinon
    """
    is_client_connectable = False
    try:
        connection = connector.connect(host = 'localhost',
                                       database = 'NaVaBe',
                                       user = 'root',
                                       password = 'Clervie2014!') # Mettez ici votre mot de passe à vous

        cursor = connection.cursor()
        request = "SELECT mot_de_passe FROM clients WHERE identifiant = " +"'" + email + "'"

        cursor.execute(request)
        mot_de_passe = cursor.fetchone()

        if not mot_de_passe is None:
            mot_de_passe = mot_de_passe[0]

            if len(mot_de_passe) > 0:
                if mot_de_passe == password:
                    is_client_connectable =True

    except connector.Error as error:
        pass

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

    return is_client_connectable

def registration():

    pass

def send_email(name:str, mail_receiver :str,message:str ='', subject:str='') -> None:
    """
    Permet d'envoyer des mails aux clients, par défaut la fonction envoie un mail de bienvenu.
    Les paramètres name et mail sont obligatoires pour le bon fonctionnement de cette fonction

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
          "Cordialement, \nLa NaVaBe Team \n".format(name,"https://localhost:5000/confirm")
    sujet = "Bienvenu Chez NaVaBe !"

    if len(message) > 0 & len(subject) > 0:
        msg = message
        sujet = subject

    message_mail = EmailMessage()
    message_mail['from'] = navabe_user_mail
    message_mail['to'] = mail_receiver
    message_mail['subject'] = sujet
    message_mail.set_content(msg)

    server = smtp.SMTP_SSL('smtp.gmail.com',465)
    server.login(navabe_user_mail, 'sortcwnjprpmlmfz')
    server.sendmail(navabe_user_mail, mail_receiver,message_mail.as_string())

if __name__ == "__main__":
   #print(is_client_connectable('Navabe@root.ca', "Projet-Glo-2005"))
   send_email("Bertrand A", "beawe@ulaval.ca")


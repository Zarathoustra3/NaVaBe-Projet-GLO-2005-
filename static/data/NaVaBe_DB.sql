/*
Assurez-vous d'être connecté à MYSQL en tant que root que la création du nouvel
utilisateur se passe convenablement (et l'accord de permissions aussi) :)
*/
CREATE DATABASE IF NOT EXISTS NAVABE; /*on crée la base de donnée qui sera utilisée pour le projet */
CREATE USER 'Navabe_Project'@'localhost';                 /*Nouvel utilisateur, cet utilisateur est utilisé dans le code python pour 
                                                    faire des requetes, donc pas besoin de modifier à chaque mise à jour
                                                    les identifiants de connection à la BDD ;)*/
IDENTIFIED WITH caching_sha2_password BY 'GLO-2005';
GRANT ALL PRIVILEGES ON NAVABE.* TO 'Navabe_Project'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES; /*On s'assure que les permissions entrent en vigueur*/

/*SHOW GRANTS FOR 'Navabe_Project'@'host';*/ /*Decommentez ici si vous souhaitez voir les privilèges*/

/*
    On peut commencé à utiliser la BD maintenant...
*/

USE NAVABE;

CREATE TABLE IF NOT EXISTS clients(email VARCHAR(45), mot_de_passe VARCHAR(45));/*Cette table c'est pour tester le login*/

/*Peuplons la pour voir*/
INSERT INTO  clients (email, mot_de_passe) 
    VALUES( 'etudiant@ulaval.ca','123456'),
          ( 'navabe@glo.ca','Glo-2005'),
          ( 'etre_humain@vivant.com', 'Vivre_bien'); /*On pourra les utiliser pour
                                                     tester la connexion du site au 
                                                     serveur MYSQL et aussi le login du site*/

/*S'il y a une restructuration que devez faire, vous pouvez le faire... et soumettre ce fichier ou (un autre) 
sur git comme ca on est sûr de travailer, tous sur les mêmes données */

/*----------------FIN POUR LE MOMENT----------------*/
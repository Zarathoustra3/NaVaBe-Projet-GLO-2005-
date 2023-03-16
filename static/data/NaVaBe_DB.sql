-- Active: 1676258416989@@127.0.0.1@3306@navabe

CREATE DATABASE IF NOT EXISTS NAVABE; /*on crée la base de donnée qui sera utilisée pour le projet */
CREATE USER 'Navabe_Project'@'localhost'; /*Nouvel utilisateur, cet utilisateur est utilisé dans le code python pour
                                                    faire des requêtes, donc pas besoin de modifier à chaque mise à jour
                                                    les identifiants de connection à la BDD ;)*/
IDENTIFIED BY 'GLO-2005';
GRANT ALL PRIVILEGES ON NAVABE.* TO 'Navabe_Project'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;

/*-----------------------------------------------------------------------------------------*/
USE NAVABE;
/*Création des tables et de leurs gâchettes(ou procédures) respectives pour permettre un maintenace à partir du web*/
CREATE TABLE clients ( numClient INT(4) UNSIGNED ZEROFILL AUTO_INCREMENT , 
                       idClient CHAR(8) NOT NULL,
                       nom VARCHAR (45) NOT NULL, 
                       prenom  VARCHAR(45) NOT NULL,
                       adresse VARCHAR (255) NOT NULL, 
                       mail VARCHAR(255) NOT NULL,  
                       PRIMARY KEY (idClient), 
                       UNIQUE KEY (numClient), 
                       UNIQUE KEY(mail));

--On lui fait un générateur de d'ID: le generateur créera l'ID à partir de 2 premieres lettres du prenom et du nom suivi de l'emplacement(en format 00001) du client dans la table.
DELIMITER //

CREATE TRIGGER ID_Clients_generator BEFORE INSERT ON clients FOR EACH ROW
BEGIN
    DECLARE Max_num INT;
    SELECT IFNULL(MAX(numClient), 0) INTO Max_num FROM clients;
    SET NEW.idClient = UPPER(CONCAT(SUBSTR(NEW.prenom, 1, 2), SUBSTR(NEW.nom, 1, 2), LPAD(Max_num + 1, 4, '0')));
END//

DELIMITER;

CREATE TABLE Livres (ISBN CHAR(13) NOT NULL, 
                    titre VARCHAR(255) NOT NULL , 
                    auteur VARCHAR(45),
                    categorie VARCHAR(45), 
                    prix FLOAT NOT NULL , 
                    annee_parution INT(4) NOT NULL,
                    synopsis VARCHAR(750), 
                    PRIMARY KEY (ISBN));

CREATE TABLE Inventaire( ISBN CHAR(13),
                         categorie VARCHAR(45), 
                         quantite INT UNSIGNED, 
                         FOREIGN KEY(ISBN) REFERENCES Livres(ISBN), 
                         UNIQUE KEY(ISBN));

--Pour ces deux tables, on utilisera la procédure ci-bas pour l'insertion des données, elle permet de mettre à jour l'inventaire directement (FINI les insertions brutes dans la table).
DELIMITER //
CREATE PROCEDURE Ajout_Livre ( IN ISBN_ CHAR(13), 
                               titre_ VARCHAR(255), 
                               auteur_ VARCHAR(45), 
                               categorie_ VARCHAR(45), 
                               prix_ FLOAT, 
                               annee_parution_ INT(4), 
                               synopsis_ VARCHAR(750))
BEGIN
    DECLARE est_present INT (1);
    SET est_present = (SELECT EXISTS (SELECT * FROM Livres WHERE `ISBN` = ISBN_));

    IF est_present = 0 THEN
        INSERT INTO Livres VALUES (ISBN_, titre_, auteur_, categorie_, prix_, annee_parution_,synopsis_);
        INSERT INTO Inventaire VALUES(ISBN_, categorie_, 1);
    ELSE
        UPDATE Inventaire SET quantite = quantite + 1 WHERE `ISBN` = ISBN_;

    END IF;     
END//

DELIMITER;

/*Fin de la procédure*/

CREATE TABLE Paniers (id INT AUTO_INCREMENT, 
                      idClient CHAR(8), 
                      ISBN CHAR(13), date_ajout DATETIME DEFAULT NOW(),
                      UNIQUE KEY (id), 
                      FOREIGN KEY (idClient) REFERENCES clients(idClient), 
                      FOREIGN KEY (ISBN) REFERENCES Inventaire(ISBN));

CREATE TABLE Facture (idFacture INT(7) UNSIGNED ZEROFILL AUTO_INCREMENT, 
                      date_facturation DATE, 
                      idClient CHAR(8), 
                      idCommande, 
                      montant DECIMAL(10, 2) UNSIGNED,
                      FOREIGN KEY (idClient) REFERENCES clients(idClient), 
                      FOREIGN KEY(idCommande) REFERENCES historique_Commande(idCommande));
"""
Dans ce fichier, se trouvent les entités que l'on aura à manipuler chez NaVaBe
Ces entités sont définies en classe (Ainsi on utilise la POO)
"""
from datetime import datetime
class Manufacturer:
    """
    Producteur manufacturier (et /ou Industriel)
    """
    def __int__(self, name:str,year_of_creation: int, address:str, city:str, country:str,
                zip_code:str, type_of_prod:str):

        self.name = name
        self.year = year_of_creation
        self.address = address
        self.city = city
        self.country = country
        self.zip_code = zip_code
        self.type_of_product =type_of_prod #type de production ou service offert

    def get_name(self):
        """
        :return: Nom du producteur
        """
        return self.name

    def get_age(self):
        """
        :return:Âge du producteur
        """
        return datetime.date().year - self.year
    def get_address(self):
        """
        :return: Adresse
        """
        return self.address
    def get_complete_address(self):
        """
        :return: Adresse complète au format Adresse, Ville, Boîte postale, Pays
        """
        return "{}, {}, {}, {}".format(self.address,self.city,
                                       self.zip_code,self.country)

    def get_city(self):
        return  self.city

    def get_country(self):
        return self.country

    def get_zipcode(self):
        """
        :return: Boite postale
        """
        return self.zip_code
    def get_type_of_product(self):
        return self.type_of_product

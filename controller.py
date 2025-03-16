from model import Shoe

class Shoecontroller:
    def __init__(self, model, view):
        self.model=model
        self.view=view

    def add_shoe(self, id, gender_type, type, color, price, brand, size):
        if price<=0:
            print("Cena musí byť vyššia ako 0 !")
        elif id in self.model.get_id_list():
            print("Tovar s týmto ID je už evidovaný.")
        else:
            shoe=Shoe(id, gender_type, type, color, price, brand, size)
            self.model.add_shoe(shoe)

    def delete_shoe(self, id):
        if id in self.model.get_id_list():
            for shoe in self.model.shoes:
                if shoe.id==id:
                    self.model.delete_shoe(shoe)

    def display_shoes(self):
        shoes=self.model.get_shoes()
        self.view.display_shoes(shoes)

    def display_shoes_by_size(self, size):
        shoes = self.model.get_shoes()
        self.view.display_shoes_by_size(shoes, size)

    def display_total_shoes_price(self):
        price = self.model.get_total_price()
        self.view.display_total_shoes_price(price)


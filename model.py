class Shoe:
    def __init__(self, id, gender_type, type, color, price, brand, size):
        self.id=id
        self.gender_type = gender_type
        self.type=type
        self.color =color
        self.price =price
        self.brand=brand
        self.size=size


class Shoemodel:
    def __init__(self):
        self.shoes=[]

    def add_shoe(self,shoe):
        self.shoes.append(shoe)

    def delete_shoe(self, shoe):
        self.shoes.remove(shoe)
    #{"id": id, "gender_type": gender_type, "type": type, "color": color, "price": price, "brand": brand, "size": size}

    def get_shoes(self):
        return self.shoes

    def get_id_list(self):
        id_list=[]
        for shoe in self.shoes:
            id_list.append(shoe.id)
        return id_list

    def get_total_price(self):
        sum=0
        for shoe in self.shoes:
            sum+=shoe.price
        return sum


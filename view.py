class Shoeview:
    def display_shoes(self, shoes):
        print("\nTopánky k dispozícii:")
        for shoe in shoes:
            print(f"{shoe.id} - {shoe.gender_type} - {shoe.type} - {shoe.color} - {shoe.price} - {shoe.brand} - {shoe.size} ")

    def display_shoes_by_size(self,shoes, size):
        print(f"\nTopánky k dispozícii veľkosti {size}:")
        for shoe in shoes:
            if shoe.size == size:
                print(f"{shoe.id} - {shoe.gender_type} - {shoe.type} - {shoe.color} - {shoe.price} - {shoe.brand} - {shoe.size} ")

    def display_total_shoes_price(self, price):
        print(f"\nCelková cena všetkých topánok v sklade je:")
        print(price)
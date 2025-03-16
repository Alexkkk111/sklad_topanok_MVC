from controller import Shoecontroller
from model import Shoemodel
from view import Shoeview

model=Shoemodel()
view=Shoeview()
controller=Shoecontroller(model, view)

controller.add_shoe('3546', 'male', 'running', 'black', 45, 'adidas', 39)
controller.add_shoe('3547', 'female', 'hiking', 'white', 55, 'nike', 38)
controller.add_shoe('3548', 'male', 'running', 'black', 61, 'reebok', 37)
controller.add_shoe('3549', 'female', 'climbing', 'green', 98, 'adidas',41)
controller.add_shoe('3541', 'male', 'running', 'blue', 100, 'puma', 42)
controller.add_shoe('3542', 'female', 'formal', 'black', 45, 'adidas', 39)
controller.add_shoe('3543', 'male', 'running', 'orange', 65, 'nike', 43)
controller.add_shoe('3544', 'female', 'tennis', 'black', 75, 'reebok', 41)
controller.add_shoe('3545', 'male', 'running', 'purple', 88, 'adidas', 40)
controller.add_shoe('3540', 'female', 'casual', 'black', 91, 'puma', 43)

controller.display_shoes()

controller.delete_shoe('3540')
controller.delete_shoe('3545')

controller.display_shoes()

controller.display_shoes_by_size(39)

controller.display_total_shoes_price()

controller.add_shoe('3541', 'female', 'casual', 'black', 91, 'puma', 43)

controller.add_shoe('3999', 'female', 'casual', 'black', 0, 'puma', 43)

controller.display_shoes()


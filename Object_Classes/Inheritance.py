# we can have class that inherit the functionality of
# other class without writing the class
# check in inheritance_class_2

from inheritance_class_def import Chef
from inheritance_class_2 import ChineseChef

myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()

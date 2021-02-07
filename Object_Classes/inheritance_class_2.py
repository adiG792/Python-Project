from inheritance_class_def import Chef


class ChineseChef(Chef):  # to inherit the attributes of other class
                          # simply write the class name in () in class classname()
    def make_special_dish(self):
        print("The chef makes orange chicken")


    def make_fried_rice(self):
        print("The chef makes fried rice")

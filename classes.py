import modules

modules.clearer()

# classes


class Rectange:
    # pass

    # functions within a class are called 'methods'
    def __init__(self, len, width):
        super().__init__()
        self.length = len
        self.width = width

    def area(self):
        return ('Area of rectangle: ', (self.length + self.width) * 2)


my_rect = Rectange(10, 5)
modules.printer(my_rect)
modules.printer(my_rect.area())

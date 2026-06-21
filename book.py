class Book:
    def __init__(self, id, title, author, quantity):
        self.id = id
        self.title = title
        self.author = author
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity

    def increase_quantity(self):
        self.__quantity += 1

    def decrease_quantity(self):
        if self.__quantity > 0:
            self.__quantity -= 1
            return True
        return False

    def show_info(self):
        print(f"{self.id} | {self.title} | {self.author} | {self.__quantity}")

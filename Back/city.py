class City:
    def __init__(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_name(self, value):
        self.__name = value


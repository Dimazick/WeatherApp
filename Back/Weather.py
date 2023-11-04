class Weather:
    def __init__(self, humidity, temp, description, pressure):
        self.__humidity = humidity
        self.__temp = temp
        self.__description = description
        self.__pressure = pressure

    def get_humidity(self):
        return self.__humidity

    def set_humidity(self, value):
        self.__humidity = value

    def get_temp(self):
        return self.__temp

    def set_temp(self, value):
        self.__temp = value

    def get_pressure(self):
        return self.__pressure

    def set_pressure(self, value):
        self.__pressure = value

    def get_description(self):
        return self.__description

    def set_description(self, value):
        self.__description = value
        
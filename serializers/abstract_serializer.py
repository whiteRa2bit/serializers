from abc import abstractmethod, ABC

class AbstractSerializer(ABC):
    def __init__(self, name, is_binary):
        self.name = name
        self.is_binary = is_binary

    @abstractmethod
    def encode(self, raw_data):
        pass

    @abstractmethod
    def decode(self, serialized_data):
        pass

    def save_data(self, serialized_data, data_path):
        mode = 'wb' if self.is_binary else 'w'
        with open(data_path, mode) as file:
            file.write(serialized_data)

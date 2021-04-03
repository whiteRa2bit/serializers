import pickle

from serializers.abstract_serializer import AbstractSerializer

class PickleSerializer(AbstractSerializer):
    def encode(self, raw_data):
        return pickle.dumps(raw_data, 2)

    def decode(self, serialized_data):
        return pickle.loads(serialized_data)

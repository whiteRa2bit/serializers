import yaml

from serializers.abstract_serializer import AbstractSerializer

class YamlSerializer(AbstractSerializer):
    def encode(self, raw_data):
        return yaml.dump(raw_data)

    def decode(self, serialized_data):
        return yaml.load(serialized_data)

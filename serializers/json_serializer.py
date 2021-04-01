import json

from serializers.abstract_serializer import AbstractSerializer

class JsonSerializer(AbstractSerializer):
    def encode(self, raw_data):
        return json.dumps(raw_data, indent=4)

    def decode(self, serialized_data):
        return json.loads(serialized_data)

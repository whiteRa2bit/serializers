import xmltodict
from dicttoxml import dicttoxml

from serializers.abstract_serializer import AbstractSerializer

class XmlSerializer(AbstractSerializer):
    def encode(self, raw_data):
        return dicttoxml(raw_data).decode()

    def decode(self, serialized_data):
        return xmltodict.parse(serialized_data)

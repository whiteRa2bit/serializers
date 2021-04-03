from serializers.abstract_serializer import AbstractSerializer
from serializers.protobuf_serializer.structure_pb2 import Struct


class ProtobufSerializer(AbstractSerializer):
    def encode(self, raw_data):
        item = self._parse_struct(raw_data)
        return item.SerializeToString()

    def decode(self, serialized_data):
        item = Struct()
        item.ParseFromString(serialized_data)
        return {
            'PackageID': item.PackageID,
            'PersonID': item.PersonID,
            'Name': item.Name,
            'CurrentLocation': item.CurrentLocation,
            'Inventory': dict(item.Inventory)
        }

    @staticmethod
    def _parse_struct(raw_data):
        item = Struct()
        item.PackageID = raw_data['PackageID']
        item.PersonID = raw_data['PersonID']
        item.Name = raw_data['Name']
        item.CurrentLocation = raw_data['CurrentLocation']

        for key, val in raw_data['Inventory'].items():
            item.Inventory[key] = val
        
        return item

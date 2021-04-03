import msgpack

from serializers.abstract_serializer import AbstractSerializer

class MsgpackSerializer(AbstractSerializer):
    def encode(self, raw_data):
        return msgpack.packb(raw_data, use_bin_type=True)

    def decode(self, serialized_data):
        return msgpack.unpackb(serialized_data, raw=False)

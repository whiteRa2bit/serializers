from io import BytesIO

import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

from serializers.abstract_serializer import AbstractSerializer
from serializers.avro_serializer.config import SCHEMA_PATH


class AvroSerializer(AbstractSerializer):
    def __init__(self, name, is_binary, schema_path=SCHEMA_PATH):
        self.name = name
        self.is_binary = is_binary
        self._schema = avro.schema.parse(open(schema_path, "rb").read())

    def encode(self, raw_data):
        byte_stream = BytesIO()
        writer = DataFileWriter(byte_stream, DatumWriter(), self._schema)
        writer.append(raw_data)
        writer.flush()
        serialized_data = byte_stream.getvalue()
        writer.close()
        return serialized_data

    def decode(self, serialized_data=None):
        byte_stream = BytesIO(serialized_data)
        reader = DataFileReader(byte_stream, DatumReader(self._schema))
        data = [item for item in reader][0]
        return data

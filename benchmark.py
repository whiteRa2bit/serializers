import json
import sys
import os

from tabulate import tabulate

from config import RAW_DATA, LOOPS, SERIALIZED_DATA_DIR, DESERIALIZED_DATA_DIR
from serializers import JsonSerializer, PickleSerializer, XmlSerializer, ProtobufSerializer, AvroSerializer, \
    YamlSerializer, MsgpackSerializer
from utils import execute_and_profile

_serializers = [
    JsonSerializer('json', is_binary=False),
    PickleSerializer('pickle', is_binary=True),
    XmlSerializer('xml', is_binary=False),
    ProtobufSerializer('protobuf', is_binary=True),
    AvroSerializer('avro', is_binary=True),
    YamlSerializer('yaml', is_binary=False),
    MsgpackSerializer('msgpack', is_binary=True)
]


def _print_results(enc_table, dec_table):
    enc_table.sort(key=lambda x: x[1])
    enc_table.insert(0, ['Package', 'Seconds', 'Size'])
    
    dec_table.sort(key=lambda x: x[1])
    dec_table.insert(0, ['Package', 'Seconds'])
    
    print ("\nEncoding Test (%d loops)" % LOOPS)
    print (tabulate(enc_table, headers="firstrow"))
    
    print ("\nDecoding Test (%d loops)" % LOOPS)
    print (tabulate(dec_table, headers="firstrow"))


def _save_data(serializer, serialized_data, deserialized_data):
    serialized_data_path = os.path.join(SERIALIZED_DATA_DIR, f"{serializer.name}_serializer.{serializer.name}")
    serializer.save_data(serialized_data, serialized_data_path)

    deserialized_data_path = os.path.join(DESERIALIZED_DATA_DIR, f"{serializer.name}_serializer.json")
    

    with open(deserialized_data_path, 'w') as file:
        file.write(json.dumps(deserialized_data, indent=4))


def main():
    enc_table = []
    dec_table = []

    print ("Running tests (%d loops each)" % LOOPS)
    for serializer in _serializers:
        serialized_data, execution_time = execute_and_profile(serializer.encode, RAW_DATA, loops=LOOPS)
        enc_table.append([serializer.name, execution_time, sys.getsizeof(serialized_data)])
        deserialized_data, execution_time = execute_and_profile(serializer.decode, serialized_data, loops=LOOPS)
        dec_table.append([serializer.name, execution_time])
        _save_data(serializer, serialized_data, deserialized_data)

    _print_results(enc_table, dec_table)


if __name__ == '__main__':
    main()

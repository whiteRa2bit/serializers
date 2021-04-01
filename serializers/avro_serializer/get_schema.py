import dataclasses

import typing

from dataclasses_avroschema import AvroModel


class Struct(AvroModel):
    "Struct"
    PackageID: int
    PersonID: int
    Name: str
    CurrentLocation: str
    Inventory: typing.Dict[str, int]

print(Struct.avro_schema())
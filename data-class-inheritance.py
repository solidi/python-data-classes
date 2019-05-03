from dataclasses import dataclass


@dataclass
class SimpleBaseClass(object):
    field_0: str = 'default'


@dataclass
class SimpleChildClass(object):
    field_0: str = 'new default'
    field_1: int = 42


example = SimpleChildClass()
print(example)

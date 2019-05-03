from dataclasses import dataclass


@dataclass
class SimpleBaseObject(object):
    field_a: any
    field_b: str


@dataclass(frozen=True)
class ImmutableSimpleDataObject(object):
    '''
    In this case,
    __init__, __repr__, __lt__, __eq__, __gt__ will all be generated automatically.
    '''
    field_a: int
    field_b: str


example = SimpleBaseObject('a', 'b')
print(example)

example2 = SimpleBaseObject(1, 'b')
print(example == example2)

example = {ImmutableSimpleDataObject(
    1, 'b'), ImmutableSimpleDataObject(2, 'c')}
print(example)

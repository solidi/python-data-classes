from dataclasses import dataclass, field
import sys


def get_argv():
    return sys.argv[1]


@dataclass
class SimpleDataObject(object):
    field_a: str
    field_b: str = field(default_factory=get_argv)

    def __post_init__(self):
        self.field_b = self.field_b.upper()


example = SimpleDataObject(field_a='a')
print(example)

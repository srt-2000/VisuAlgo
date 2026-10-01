import copy
from dataclasses import dataclass, fields, MISSING


@dataclass
class BaseAlgorithmLogDTO:
    """Base class of AlgorithmDTO objects for strict type checking,
    clear() method need to make attributes to default.
    """

    def clear(self)-> None:
        subclass_fields = fields(self)

        for field in subclass_fields:

            if field.default is not MISSING:
                setattr(self, field.name, copy.deepcopy(field.default))
            elif field.default_factory is not MISSING:
                setattr(self, field.name, field.default_factory())
            else:
                setattr(self, field.name, None)

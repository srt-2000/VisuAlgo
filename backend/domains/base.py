"""Shared base for algorithm logs stored as one list per column."""

import copy
from dataclasses import MISSING, dataclass, fields


@dataclass
class BaseAlgorithmLogDTO:
    """Log that stores every step as the next item in parallel lists.

    Subclasses add the columns they need. Call ``clear()`` before a
    new run so old steps do not stay in those lists.
    """

    def clear(self) -> None:
        """Reset every field to its declared default.

        A plain default is copied back. A ``default_factory`` field
        (usually a list) becomes a fresh empty list. A field with
        no default becomes ``None``.
        """
        subclass_fields = fields(self)

        for field in subclass_fields:
            if field.default is not MISSING:
                setattr(self, field.name, copy.deepcopy(field.default))
            elif field.default_factory is not MISSING:
                setattr(self, field.name, field.default_factory())
            else:
                setattr(self, field.name, None)

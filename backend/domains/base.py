from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class BaseStepValueObject:
    """Base class of StepValueObjects for strict type checking,
    frozen=True and slots=True are bounden for subclasses.
    """
    pass
import abc
from abc import ABC, abstractmethod

class AbstractBackoff(ABC, metaclass=abc.ABCMeta):
    def reset(self) -> None: ...
    @abstractmethod
    def compute(self, failures): ...

class ConstantBackoff(AbstractBackoff):
    def __init__(self, backoff) -> None: ...
    def compute(self, failures): ...

class NoBackoff(ConstantBackoff):
    def __init__(self) -> None: ...

class ExponentialBackoff(AbstractBackoff):
    def __init__(self, cap, base) -> None: ...
    def compute(self, failures): ...

class FullJitterBackoff(AbstractBackoff):
    def __init__(self, cap, base) -> None: ...
    def compute(self, failures): ...

class EqualJitterBackoff(AbstractBackoff):
    def __init__(self, cap, base) -> None: ...
    def compute(self, failures): ...

class DecorrelatedJitterBackoff(AbstractBackoff):
    def __init__(self, cap, base) -> None: ...
    def reset(self) -> None: ...
    def compute(self, failures): ...

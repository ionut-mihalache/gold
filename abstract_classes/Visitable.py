from __future__ import annotations
from abc import abstractmethod

from abstract_classes.Visitor import Visitor


class Visitable:
    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass

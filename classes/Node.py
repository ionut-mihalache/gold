from __future__ import annotations
from abc import abstractmethod, ABC

from abstract_classes import Visitor


class Node(ABC):
    
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass

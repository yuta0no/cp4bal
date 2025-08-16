from abc import ABC, abstractmethod

from jaxtyping import Array, Int


class Acquisition(ABC):
    @abstractmethod
    def select(self, budget: int) -> Array[Int, " budget"]:
        pass

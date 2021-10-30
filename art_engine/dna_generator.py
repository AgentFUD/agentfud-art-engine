from abc import ABC, abstractmethod
from typing import List, Optional, Tuple
from itertools import product
import random


class DNAGeneratorStrategy(ABC):
    @abstractmethod
    def generate_dnas(
        self, traits: List[str], trait_options: List[dict], quantity: int
    ) -> List[dict]:
        pass


class SequentialGenerator(DNAGeneratorStrategy):
    def generate_dnas(
        self, traits: List[str], trait_options: List[dict], quantity: int
    ) -> List[dict]:
        ordered_trait_options = [trait_options[val] for val in traits]
        dnas = []
        for x in product(*ordered_trait_options):
            y = zip(traits, list(x))
            dnas.append(dict(y))
        return dnas[:quantity]


class RandomGenerator(ABC):
    def generate_dnas(
        self, traits: List[str], trait_options: List[str], quantity: int
    ) -> List[dict]:
        ordered_trait_options = [trait_options[val] for val in traits]
        dnas = []
        for x in product(*ordered_trait_options):
            y = zip(traits, list(x))
            dnas.append(dict(y))
        random.shuffle(dnas)
        return dnas[:quantity]


class RarityWeightGenerator(ABC):
    def generate_dnas(
        self, traits: List[str], trait_options: List[str], quantity: int
    ) -> List[dict]:
        pass

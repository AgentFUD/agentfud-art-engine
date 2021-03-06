from abc import ABC, abstractmethod
from typing import List, Optional
from itertools import product
import random
import json
import sys
import hashlib
from rich import print
from art_engine.appconfig import RARITY_JSON_NAME


class SimpleDNAGeneratorStrategy(ABC):
    @abstractmethod
    def generate_dnas(
        self,
        traits: List[str],
        trait_options: List[dict],
        collection_size: int,
        retries: Optional[int],
    ) -> List[dict]:
        pass


class RetryDNAGeneratorStrategy(ABC):
    @abstractmethod
    def generate_dnas(
        self,
        traits: List[str],
        trait_options: List[dict],
        collection_size: int,
        retries: int,
    ) -> List[dict]:
        pass


class SequentialGenerator(SimpleDNAGeneratorStrategy):
    def generate_dnas(
        self,
        traits: List[str],
        trait_options: List[dict],
        collection_size: int,
        retries: Optional[int],
    ) -> List[dict]:
        ordered_trait_options = [trait_options[val] for val in traits]
        dnas = []
        for x in product(*ordered_trait_options):
            y = zip(traits, list(x))
            dnas.append(dict(y))
        return dnas[:collection_size]


class RandomGenerator(SimpleDNAGeneratorStrategy):
    def generate_dnas(
        self,
        traits: List[str],
        trait_options: List[str],
        collection_size: int,
        retries: Optional[int],
    ) -> List[dict]:
        ordered_trait_options = [trait_options[val] for val in traits]
        dnas = []
        for x in product(*ordered_trait_options):
            y = zip(traits, list(x))
            dnas.append(dict(y))
        random.shuffle(dnas)
        return dnas[:collection_size]


class RarityWeightGenerator(RetryDNAGeneratorStrategy):
    def hash_dna(self, dna):
        return hashlib.sha1(json.dumps(dna, sort_keys=True).encode("UTF-8")).hexdigest()

    def generate_dnas(
        self,
        traits: List[str],
        trait_options: List[str],
        collection_size: int,
        retries: int,
    ) -> List[dict]:
        try:
            with open(RARITY_JSON_NAME, "r") as file:
                rarities = json.load(file)
        except FileNotFoundError:
            print("-" * 75)
            print(
                f"[gold3]Rarity configuration file[/gold3] [blue]{RARITY_JSON_NAME}[/blue] [gold3]can not be found. Terminating.[/gold3]"
            )
            print("-" * 75)
            sys.exit()

        existing_dna_hashes = []
        dnas = []
        for d in range(collection_size + retries):
            dnax = {}
            for n in traits:
                dnax[n] = random.choices(
                    trait_options[n], weights=rarities[n].values(), k=1
                )[0]
            h = self.hash_dna(dnax)
            if h not in existing_dna_hashes:
                existing_dna_hashes.append(h)
                dnas.append(dnax)
        return dnas[:collection_size]

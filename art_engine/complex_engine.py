import os, math, json, time
from PIL import Image
from art_engine.dna_generator import (
    SequentialGenerator,
    RandomGenerator,
    RarityWeightGenerator,
)
from art_engine.appconfig import complex_project_template


class ComplexEngine:
    def __init__(self, config) -> None:
        self.config = config
        self.dnas = []
        self.sprite_configs = []
        self.trait_options = {}
        self.max_possible_combinations = 0
        self.dna_generator = None

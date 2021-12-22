import os, math, json, time
from PIL import Image
from art_engine.dna_generator import (
    SequentialGenerator,
    RandomGenerator,
    RarityWeightGenerator,
)
from art_engine.appconfig import simple_project_template


class SimpleEngine:
    def __init__(self, config) -> None:
        self.config = config
        self.dnas = []
        self.sprite_configs = []
        self.trait_options = {}
        self.max_possible_combinations = 0
        self.dna_generator = None

    def setup_engine(self):
        self.check_config_file_values()
        self.collect_trait_options()
        self.calculate_max_possible_combinations()

        if self.config.dna_generation_type == 1:
            self.dna_generator = SequentialGenerator()
        if self.config.dna_generation_type == 2:
            self.dna_generator = RandomGenerator()
        if self.config.dna_generation_type == 3:
            self.dna_generator = RarityWeightGenerator()

    def check_config_file_values(self):
        try:
            assert self.config.engine_type == "simple"
        except:
            raise Exception("engine_type must be simple in your instance_config.py")

        try:
            assert self.config.base_image is not None
            assert os.path.isfile(self.config.base_image) == True
        except:
            raise Exception("Check your base_image in your instance_config.py")

        try:
            assert type(self.config.traits) == list
            assert len(self.config.traits) > 0
        except:
            raise Exception(
                "traits in instance_config.py must exists and can not be empty"
            )

        try:
            assert self.config.dna_generation_type in [1, 2, 3]
        except:
            raise Exception(
                "DNA generation type must be 1, 2 or 3 in instance_config.py"
            )

    def collect_trait_options(self):
        self.trait_options = {
            trait_name: [
                os.path.splitext(x)[0]
                for x in os.listdir(
                    simple_project_template["simple_layers"] + "/" + trait_name
                )
            ]
            for trait_name in self.config.traits
        }

    def calculate_max_possible_combinations(self):
        self.max_possible_combinations = math.prod(
            [len(self.trait_options[t]) for t in self.trait_options]
        )

    def generate_dnas(self, collection_size, retries) -> None:
        self.dnas = self.dna_generator.generate_dnas(
            traits=self.config.traits,
            trait_options=self.trait_options,
            collection_size=collection_size,
            retries=retries,
        )

    def save_dnas(self) -> None:
        if len(self.dnas) == 0:
            return
        with open(
            self.config.simple_project_template["cache"] + "/metadata.json", "w"
        ) as f:
            f.write(json.dumps(self.dnas))

    def load_dnas(self) -> None:
        with open(
            self.config.simple_project_template["cache"] + "/metadata.json", "r"
        ) as f:
            self.dnas = json.load(f)

    def generate_sprite_configs(self) -> None:
        for dna in self.dnas:
            sprite_config = []
            for trait_name, trait_value in dna.items():
                sprite_config.append(
                    f"{self.config.simple_project_template['simple_layers']}/{trait_name}/{trait_value}.png"
                )
            self.sprite_configs.append(sprite_config)

    def generate_rarity_config(self):
        rarity_config = {}
        for trait in self.trait_options:
            rarity_config[trait] = {}
            for gene in self.trait_options[trait]:
                rarity_config[trait][gene] = 1

        with open(self.config.RARITY_JSON_NAME, "w", encoding="utf-8") as f:
            json.dump(rarity_config, f, ensure_ascii=False, indent=4)

    def build_metadata(self, id, dna) -> None:
        atributes = []
        for d in dna:
            if hasattr(self.config, "traits_excluded_from_metadata"):
                if d in self.config.traits_excluded_from_metadata:
                    continue
            atributes.append({"trait_type": d, "value": dna[d]})
        metadata = {
            "name": f"{self.config.item_name} #{id}",
            "description": self.config.description,
            "image": f"{self.config.image_url}/{id}.png",
            "date": f"{int(time.time())}",
            "attributes": atributes,
            "engine": self.config.engine_name,
        }
        with open(
            f"{self.config.simple_project_template['built_metadata']}/{id}.json",
            "w",
            encoding="utf-8",
        ) as f:
            json.dump(metadata, f, ensure_ascii=False, indent=4)
        return metadata

    def build_image(self, id, sprite_config) -> None:
        base_image = Image.open(self.config.base_image).convert("RGBA")
        for i, sprite in enumerate(sprite_config):
            next_image = Image.open(sprite).convert("RGBA")
            base_image.paste(next_image, (0, 0), next_image)
        result = base_image.resize(self.config.image_size)
        result.save(
            f"{self.config.simple_project_template['built_images']}/{id}.png", "PNG"
        )

from PIL import Image

import math, random, json, time
import os


class ArtEngine:
    def __init__(self, config) -> None:
        self.config = config
        self.dnas = []
        self.sprite_configs = []
        self.trait_options = {}
        self.max_possible_combinations = 0

        self.prepare_trait_options()
        self.calculate_max_possible_combinations()

    def calculate_max_possible_combinations(self):
        self.max_possible_combinations = math.prod(
            [len(self.trait_options[t]) for t in self.trait_options]
        )

    def prepare_trait_options(self):
        self.trait_options = {
            trait_name: [
                os.path.splitext(x)[0]
                for x in os.listdir("./layers/simple/" + trait_name)
            ]
            for trait_name in self.config.traits
            if trait_name != "Color"
        }
        self.trait_options["Color"] = self.config.available_colors

    def generate_dnas(self, max_items=10) -> None:
        for i in range(max_items):
            dna = {}
            for t in self.config.traits:
                dna[t] = self.trait_options[t][
                    random.randint(0, len(self.trait_options[t]) - 1)
                ]
            self.dnas.append(dna)

    def generate_sprite_configs(self) -> None:
        for dna in self.dnas:
            sprite_config = []
            for trait_name, trait_value in dna.items():
                if trait_name == "Color":
                    for trn in self.config.colors[trait_value]:
                        img_name = dna[trn]
                        sprite_config.append(
                            f"./layers/complex/Color/{trait_value}/{trn}/{img_name}.png"
                        )
                else:
                    sprite_config.append(
                        f"./layers/simple/{trait_name}/{trait_value}.png"
                    )
            self.sprite_configs.append(sprite_config)

    def generate_rarity_config(self):
        print("Generating rarity configuration")
        rarity_config = {}
        for trait in self.trait_options:
            rarity_config[trait] = {}
            for gene in self.trait_options[trait]:
                rarity_config[trait][gene] = 1

        with open(self.config.RARITY_JSON_NAME, "w", encoding="utf-8") as f:
            json.dump(rarity_config, f, ensure_ascii=False, indent=4)
        print("Done...")

    def build_image(self, id, sprite_config) -> None:
        base_image = Image.open("./layers/simple/Background Color/LightBlue.png")
        for i, sprite in enumerate(sprite_config):
            next_image = Image.open(sprite)
            base_image.paste(next_image, (0, 0), next_image)
        result = base_image.resize(self.config.image_size)
        print(f"./build/images/{id}.png")
        result.save(f"./build/images/{id}.png")

    def build_metadata(self, id, dna) -> None:
        atributes = []
        for d in dna:
            atributes.append({"trait_type": d, "value": dna[d]})
        metadata = {
            "name": f"{self.config.item_name} #{id}",
            "description": self.config.description,
            "image": f"https://myhost.io/images/{id}.png",
            "date": f"{int(time.time())}",
            "attributes": atributes,
            "engine": self.config.engine_name,
        }
        print(f"./build/metadata/{id}.json")
        with open(f"./build/metadata/{id}.json", "w", encoding="utf-8") as f:
            json.dump(metadata, f, ensure_ascii=False, indent=4)
        return metadata
